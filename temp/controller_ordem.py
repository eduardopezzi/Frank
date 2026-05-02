import datetime
from typing import List, Optional, Dict
import logging
from dataclasses import dataclass, field

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SistemaException(Exception):
    """Exceção base para o sistema de otimização"""
    pass

class ValidacaoException(SistemaException):
    """Exceção para erros de validação de dados"""
    pass

@dataclass
class Equipamento:
    """Representa um equipamento de usinagem"""
    id: int
    nome: str
    capacidade_max: int  # em KG
    velocidade: float  # KG/hora
    status: str = "disponível"  # disponível, ocupado, manutenção
    carga_atual: float = 0.0
    tempo_ocupado: float = 0.0  # horas ocupadas no dia
    
    def __post_init__(self):
        if self.capacidade_max <= 0:
            raise ValidacaoException("Capacidade máxima deve ser positiva")
        if self.velocidade <= 0:
            raise ValidacaoException("Velocidade deve ser positiva")
        if self.carga_atual < 0:
            raise ValidacaoException("Carga atual não pode ser negativa")
    
    def pode_processar(self, carga: float) -> bool:
        """Verifica se o equipamento pode processar a carga"""
        return (self.status == "disponível" and 
                self.carga_atual + carga <= self.capacidade_max)
    
    def processar_carga(self, carga: float, tempo: float) -> bool:
        """Processa uma carga no equipamento"""
        if self.pode_processar(carga):
            self.carga_atual += carga
            self.tempo_ocupado += tempo
            if self.carga_atual >= self.capacidade_max * 0.95:
                self.status = "ocupado"
            logger.info(f"Equipamento {self.id} processou {carga}KG em {tempo:.1f}h")
            return True
        return False
    
    def liberar(self):
        """Libera o equipamento para novo uso"""
        self.carga_atual = 0.0
        self.status = "disponível"
        logger.info(f"Equipamento {self.id} liberado")

@dataclass
class Ordem:
    """Representa uma ordem de produção"""
    id: int
    nome: str
    peso_total: float  # em KG
    quantidade: int
    tempo_estimado: float  # horas
    prazo: datetime.datetime
    prioridade: int = 1  # 1=baixa, 2=media, 3=alta, 4=urgente
    equipamentos: List[int] = field(default_factory=list)
    status: str = "pendente"  # pendente, em_processamento, concluída, atrasada
    
    def __post_init__(self):
        if self.peso_total <= 0:
            raise ValidacaoException("Peso total deve ser positivo")
        if self.quantidade <= 0:
            raise ValidacaoException("Quantidade deve ser positiva")
        if self.tempo_estimado <= 0:
            raise ValidacaoException("Tempo estimado deve ser positivo")
        if self.prazo < datetime.datetime.now():
            logger.warning(f"Ordem {self.id} com prazo no passado")
    
    def calcular_urgencia(self) -> float:
        """Calcula a urgência com base no prazo e prioridade"""
        tempo_restante = (self.prazo - datetime.datetime.now()).total_seconds() / 3600
        if tempo_restante <= 0:
            return 1000.0 * self.prioridade  # Muito urgente se já passou do prazo
        
        # Quanto menor o tempo restante, maior a urgência
        urgencia_base = 100.0 / max(tempo_restante, 1)
        return urgencia_base * self.prioridade
    
    def esta_atrasada(self) -> bool:
        """Verifica se a ordem está atrasada"""
        return datetime.datetime.now() > self.prazo

@dataclass
class Escalonamento:
    """Representa o escalonamento de uma ordem"""
    ordem: Ordem
    equipamentos: List[Equipamento]
    tempo_inicio: datetime.datetime
    tempo_fim: datetime.datetime
    carga_por_equipamento: Dict[int, float] = field(default_factory=dict)
    
    def calcular_duracao_total(self) -> float:
        """Calcula a duração total do escalonamento"""
        return (self.tempo_fim - self.tempo_inicio).total_seconds() / 3600
    
    def calcular_eficiencia(self) -> float:
        """Calcula a eficiência do escalonamento"""
        if self.ordem.tempo_estimado == 0:
            return 1.0
        return self.ordem.tempo_estimado / self.calcular_duracao_total()

@dataclass
class MetricasDesempenho:
    """Métricas de desempenho do sistema"""
    tempo_medio_processamento: float = 0.0
    utilizacao_media_equipamentos: float = 0.0
    taxa_atraso: float = 0.0
    throughput: float = 0.0  # ordens por hora
    ordens_processadas: int = 0
    ordens_atrasadas: int = 0
    
    def calcular(self, ordens_processadas: List[Ordem], 
                  equipamentos: List[Equipamento],
                  tempo_total: float) -> None:
        """Calcula todas as métricas"""
        if not ordens_processadas:
            return
        
        # Tempo médio de processamento
        self.ordens_processadas = len(ordens_processadas)
        self.ordens_atrasadas = sum(1 for o in ordens_processadas if o.esta_atrasada())
        self.taxa_atraso = (self.ordens_atrasadas / self.ordens_processadas) * 100 if self.ordens_processadas > 0 else 0
        
        # Utilização média dos equipamentos
        if equipamentos:
            utilizacao_total = sum(e.tempo_ocupado for e in equipamentos)
            capacidade_total = len(equipamentos) * 24  # 24 horas por dia
            self.utilizacao_media_equipamentos = (utilizacao_total / capacidade_total) * 100
        
        # Throughput
        if tempo_total > 0:
            self.throughput = self.ordens_processadas / tempo_total
        
        logger.info(f"Métricas calculadas: {self}")

class OtimizadorCarga:
    """Classe principal para otimização de carga de usinagem"""
    
    def __init__(self):
        self.equipamentos: Dict[int, Equipamento] = {}
        self.ordens_pendentes: List[Ordem] = []
        self.ordens_em_processamento: List[Ordem] = []
        self.ordens_concluidas: List[Ordem] = []
        self.escalonamentos: List[Escalonamento] = []
        self.metricas = MetricasDesempenho()
    
    def adicionar_equipamento(self, equipamento: Equipamento) -> None:
        """Adiciona um equipamento ao sistema"""
        self.equipamentos[equipamento.id] = equipamento
        logger.info(f"Equipamento {equipamento.id} adicionado ao sistema")
    
    def adicionar_ordem(self, ordem: Ordem) -> None:
        """Adiciona uma ordem ao sistema"""
        self.ordens_pendentes.append(ordem)
        logger.info(f"Ordem {ordem.id} adicionada ao sistema")
    
    def obter_equipamentos_disponiveis(self) -> List[Equipamento]:
        """Retorna lista de equipamentos disponíveis"""
        return [e for e in self.equipamentos.values() if e.status == "disponível"]
    
    def obter_equipamentos_compativel(self, ordem: Ordem) -> List[Equipamento]:
        """Retorna equipamentos compatíveis com a ordem"""
        disponiveis = self.obter_equipamentos_disponiveis()
        if ordem.equipamentos:
            # Filtra apenas equipamentos especificados
            return [e for e in disponiveis if e.id in ordem.equipamentos]
        return disponiveis
    
    def ordenar_ordens_por_prioridade(self) -> List[Ordem]:
        """Ordena ordens pendentes por prioridade e urgência"""
        return sorted(self.ordens_pendentes, 
                       key=lambda o: (-o.prioridade, -o.calcular_urgencia()))
    
    def escalonar_ordem_sequencial(self, ordem: Ordem) -> Optional[Escalonamento]:
        """Escalona uma ordem usando um único equipamento mais rápido"""
        equipamentos = self.obter_equipamentos_compativel(ordem)
        if not equipamentos:
            logger.warning(f"Nenhum equipamento disponível para ordem {ordem.id}")
            return None
        
        # Seleciona o equipamento mais rápido (maior velocidade)
        equipamento = max(equipamentos, key=lambda e: e.velocidade)
        
        if equipamento.pode_processar(ordem.peso_total):
            tempo_necessario = ordem.peso_total / equipamento.velocidade
            
            # Calcula o horário de início (agora + tempo de espera)
            tempo_inicio = datetime.datetime.now()
            tempo_fim = tempo_inicio + datetime.timedelta(hours=tempo_necessario)
            
            # Processa a carga
            if equipamento.processar_carga(ordem.peso_total, tempo_necessario):
                # Cria o escalonamento
                escalonamento = Escalonamento(
                    ordem=ordem,
                    equipamentos=[equipamento],
                    tempo_inicio=tempo_inicio,
                    tempo_fim=tempo_fim,
                    carga_por_equipamento={equipamento.id: ordem.peso_total}
                )
                
                # Atualiza status
                ordem.status = "em_processamento"
                self.ordens_pendentes.remove(ordem)
                self.ordens_em_processamento.append(ordem)
                self.escalonamentos.append(escalonamento)
                
                logger.info(f"Ordem {ordem.id} escalonada sequencialmente no equipamento {equipamento.id}")
                return escalonamento
        
        return None
    
    def escalonar_ordem_paralela(self, ordem: Ordem) -> Optional[Escalonamento]:
        """Escalona uma ordem dividindo a carga entre múltiplos equipamentos"""
        equipamentos = self.obter_equipamentos_compativel(ordem)
        if not equipamentos:
            return None
        
        # Filtra equipamentos que podem processar parte da carga
        capacidade_total = sum(e.capacidade_max for e in equipamentos)
        if capacidade_total < ordem.peso_total:
            logger.warning(f"Capacidade insuficiente para ordem {ordem.id}")
            return None
        
        # Divide a carga proporcionalmente
        carga_por_equipamento = {}
        carga_restante = ordem.peso_total
        
        for equipamento in equipamentos:
            if carga_restante <= 0:
                break
            
            # Calcula a carga que este equipamento pode processar
            carga_max = min(equipamento.capacidade_max, carga_restante)
            carga_proporcional = (ordem.peso_total * equipamento.capacidade_max) / capacidade_total
            
            # Usa o menor entre a capacidade máxima e a carga proporcional
            carga_alocada = min(carga_max, carga_proporcional, carga_restante)
            
            if carga_alocada > 0 and equipamento.pode_processar(carga_alocada):
                carga_por_equipamento[equipamento.id] = carga_alocada
                carga_restante -= carga_alocada
        
        if carga_restante > 0:
            logger.warning(f"Carga restante não alocada: {carga_restante}KG")
            return None
        
        # Processa em todos os equipamentos
        equipamentos_utilizados = []
        for equip_id, carga in carga_por_equipamento.items():
            equipamento = self.equipamentos[equip_id]
            tempo = carga / equipamento.velocidade
            if equipamento.processar_carga(carga, tempo):
                equipamentos_utilizados.append(equipamento)
        
        if not equipamentos_utilizados:
            return None
        
        # Calcula tempo total (baseado no equipamento mais lento)
        tempo_total = max(carga / self.equipamentos[e_id].velocidade 
                          for e_id, carga in carga_por_equipamento.items())
        
        tempo_inicio = datetime.datetime.now()
        tempo_fim = tempo_inicio + datetime.timedelta(hours=tempo_total)
        
        # Cria o escalonamento
        escalonamento = Escalonamento(
            ordem=ordem,
            equipamentos=equipamentos_utilizados,
            tempo_inicio=tempo_inicio,
            tempo_fim=tempo_fim,
            carga_por_equipamento=carga_por_equipamento
        )
        
        # Atualiza status
        ordem.status = "em_processamento"
        self.ordens_pendentes.remove(ordem)
        self.ordens_em_processamento.append(ordem)
        self.escalonamentos.append(escalonamento)
        
        logger.info(f"Ordem {ordem.id} escalonada em paralelo em {len(equipamentos_utilizados)} equipamentos")
        return escalonamento
    
    def processar_ordens(self) -> None:
        """Processa todas as ordens pendentes"""
        ordens = self.ordenar_ordens_por_prioridade()
        
        for ordem in ordens:
            # Tenta escalonamento paralelo primeiro
            escalonamento = self.escalonar_ordem_paralela(ordem)
            
            # Se não for possível, tenta escalonamento sequencial
            if not escalonamento:
                escalonamento = self.escalonar_ordem_sequencial(ordem)
            
            if escalonamento:
                logger.info(f"Ordem {ordem.id} escalonada com sucesso")
            else:
                logger.warning(f"Não foi possível escalar ordem {ordem.id}")
    
    def verificar_conclusao_ordens(self) -> None:
        """Verifica se ordens em processamento podem ser concluídas"""
        agora = datetime.datetime.now()
        ordens_para_concluir = []
        
        for ordem in self.ordens_em_processamento:
            # Encontra o escalonamento da ordem
            escalonamento = next((e for e in self.escalonamentos if e.ordem.id == ordem.id), None)
            
            if escalonamento and agora >= escalonamento.tempo_fim:
                ordens_para_concluir.append(ordem)
        
        for ordem in ordens_para_concluir:
            self.concluir_ordem(ordem)
    
    def concluir_ordem(self, ordem: Ordem) -> None:
        """Conclui uma ordem e libera os equipamentos"""
        ordem.status = "concluída" if not ordem.esta_atrasada() else "atrasada"
        
        # Encontra o escalonamento e libera os equipamentos
        escalonamento = next((e for e in self.escalonamentos if e.ordem.id == ordem.id), None)
        if escalonamento:
            for equipamento in escalonamento.equipamentos:
                equipamento.liberar()
        
        # Move para ordens concluídas
        self.ordens_em_processamento.remove(ordem)
        self.ordens_concluidas.append(ordem)
        
        logger.info(f"Ordem {ordem.id} concluída ({ordem.status})")
    
    def executar_simulacao(self, duracao_horas: float = 24.0) -> Dict:
        """Executa uma simulação do sistema por um período determinado"""
        logger.info(f"Iniciando simulação por {duracao_horas} horas")
        
        tempo_inicio = datetime.datetime.now()
        tempo_fim = tempo_inicio + datetime.timedelta(hours=duracao_horas)
        
        # Processa ordens iniciais
        self.processar_ordens()
        
        # Simula o tempo passando
        while datetime.datetime.now() < tempo_fim:
            # Verifica conclusão de ordens
            self.verificar_conclusao_ordens()
            
            # Processa novas ordens se houver equipamentos disponíveis
            if self.obter_equipamentos_disponiveis() and self.ordens_pendentes:
                self.processar_ordens()
            
            # Simula passagem do tempo (em uma implementação real, isso seria assíncrono)
            datetime.datetime.now()  # Apenas para manter o fluxo
        
        # Calcula métricas finais
        self.metricas.calcular(
            self.ordens_concluidas,
            list(self.equipamentos.values()),
            duracao_horas
        )
        
        # Retorna resultados da simulação
        resultados = {
            "tempo_simulacao": duracao_horas,
            "ordens_concluidas": len(self.ordens_concluidas),
            "ordens_atrasadas": self.metricas.ordens_atrasadas,
            "taxa_atraso": self.metricas.taxa_atraso,
            "utilizacao_equipamentos": self.metricas.utilizacao_media_equipamentos,
            "throughput": self.metricas.throughput,
            "escalonamentos": len(self.escalonamentos)
        }
        
        logger.info(f"Simulação concluída: {resultados}")
        return resultados

# Função principal para demonstração
def main():
    """Função principal para demonstração do sistema"""
    logger.info("Iniciando Sistema de Otimização de Carga de Usinagem")
    
    # Criar otimizador
    otimizador = OtimizadorCarga()
    
    # Adicionar equipamentos (baseado nos dados fornecidos)
    equipamentos_data = [
        (1, "Torno CNC 1", 1000, 50),
        (2, "Fresa Vertical 1", 800, 40),
        (3, "Plaina Lam. 1", 1200, 60),
        (4, "Serra Fita 1", 600, 30),
        (5, "Torno CNC 2", 1000, 50),
    ]
    
    for eq_id, nome, capacidade, velocidade in equipamentos_data:
        equipamento = Equipamento(id=eq_id, nome=nome, 
                                capacidade_max=capacidade, 
                                velocidade=velocidade)
        otimizador.adicionar_equipamento(equipamento)
    
    # Adicionar ordens (exemplos)
    agora = datetime.datetime.now()
    ordens_data = [
        (1, "Peça A", 500, 10, 10, agora + datetime.timedelta(hours=12), 2, [1, 2]),
        (2, "Peça B", 800, 5, 16, agora + datetime.timedelta(hours=8), 3, [1, 3]),
        (3, "Peça C", 300, 20, 6, agora + datetime.timedelta(hours=24), 1, [2, 4]),
        (4, "Peça D", 1200, 2, 24, agora + datetime.timedelta(hours=48), 1, [1, 3, 4]),
        (5, "Peça E", 600, 8, 12, agora + datetime.timedelta(hours=6), 4, [1, 2, 3]),
    ]
    
    for ord_id, nome, peso, qtd, tempo, prazo, prioridade, equipamentos in ordens_data:
        ordem = Ordem(id=ord_id, nome=nome, peso_total=peso, quantidade=qtd,
                    tempo_estimado=tempo, prazo=prazo, prioridade=prioridade,
                    equipamentos=equipamentos)
        otimizador.adicionar_ordem(ordem)
    
    # Executar simulação
    resultados = otimizador.executar_simulacao(duracao_horas=24.0)
    
    # Exibir resultados
    print("\n" + "="*50)
    print("RESULTADOS DA SIMULAÇÃO")
    print("="*50)
    print(f"Tempo de simulação: {resultados['tempo_simulacao']:.1f} horas")
    print(f"Ordens concluídas: {resultados['ordens_concluidas']}")
    print(f"Ordens atrasadas: {resultados['ordens_atrasadas']}")
    print(f"Taxa de atraso: {resultados['taxa_atraso']:.1f}%")
    print(f"Utilização dos equipamentos: {resultados['utilizacao_equipamentos']:.1f}%")
    print(f"Throughput: {resultados['throughput']:.2f} ordens/hora")
    print(f"Escalonamentos realizados: {resultados['escalonamentos']}")
    
    # Exibir detalhes dos escalonamentos
    print("\nDetalhes dos Escalonamentos:")
    print("-" * 40)
    for i, esc in enumerate(otimizador.escalonamentos[:5], 1):  # Limita aos 5 primeiros
        print(f"{i}. Ordem {esc.ordem.id} ({esc.ordem.nome})")
        print(f"   Equipamentos: {[e.id for e in esc.equipamentos]}")
        print(f"   Duração: {esc.calcular_duracao_total():.1f} horas")
        print(f"   Eficiência: {esc.calcular_eficiencia():.2f}")
        print()
    
    return otimizador

if __name__ == "__main__":
    main()
