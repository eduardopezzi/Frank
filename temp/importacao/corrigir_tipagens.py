#!/usr/bin/env python3
"""
Script para analisar e corrigir tipagens em arquivo JSON de produtos.

Uso:
    python corrigir_tipagens.py <arquivo_entrada.json> 

"""

import json
import sys
from typing import List, Dict, Any

# Dicionário modelo para definição das regras de transformação
MODELO_COLUNAS = {
    'id_erp': {
        'tipo': 'str',
        'obrigatorio': True
    },
    'codigo_barra': {
        'tipo': 'str',
        'obrigatorio': True
    },
    'nome': {
        'tipo': 'str',
        'obrigatorio': True
    },
    'tempo': {
        'tipo': 'int',
        'obrigatorio': False,
        'tratamento_erro': 'usar_zero'
    },    
    'peso': {
        'tipo': 'float',
        'obrigatorio': False,
    },
    'equipamentos': {
        'tipo': 'list',
        'obrigatorio': False
    },
    'equipamento': {
        'tipo': 'int',
        'obrigatorio': False
    }

}

def aplicar_transformacao(valor: Any, tipo: str, tratamento_erro: str = None) -> Any:
    """
    Aplica a transformação de tipo conforme especificado.
    
    Args:
        valor: Valor a ser transformado
        tipo: Tipo desejado ('str', 'int', 'float')
        tratamento_erro: Como tratar erros de conversão
        
    Returns:
        Valor transformado
    """
    if valor is None:
        if tipo == 'str':
            return ""
        elif tipo == 'int':
            return 0
        elif tipo == 'float':
            return 0.0
        elif tipo == 'list':
            return []
        else:
            pass  # Continuar para o bloco try
    
    try:
        if tipo == 'str':
            return str(valor)
        elif tipo == 'int':
            return int(valor)
        elif tipo == 'float':
            return float(str(valor).replace(',', '.'))
        elif tipo == 'list':
            if isinstance(valor, list):
                return valor
            else:
                raise ValueError(f"Valor {valor} não é uma lista")
        else:
            raise ValueError(f"Tipo desconhecido: {tipo}")
        
    except (ValueError, TypeError):
        if tratamento_erro == 'usar_zero' and tipo == 'int':
            return 0
        elif tratamento_erro == 'usar_zero_float' and tipo == 'float':
            return 0.0
        else:
            raise ValueError(f"Não foi possível converter {valor} para {tipo}")

def validar_e_corrigir_tipagem(dados: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Analisa uma lista de dicionários JSON e corrige as tipagens dos atributos.
    
    Args:
        dados: Lista de dicionários contendo os dados a serem validados
        
    Returns:
        Lista de dicionários com as tipagens corrigidas
        
    Raises:
        ValueError: Se algum dado não puder ser corrigido
    """
    dados_corrigidos = []
    erros = []
    
    for i, item in enumerate(dados):
        try:
            item_corrigido = {}
            campos_faltantes = []
            
            # Iterar sobre o modelo de colunas para validar e corrigir cada campo
            for coluna, regras in MODELO_COLUNAS.items():
                if coluna in item:
                    try:
                        if coluna == 'equipamento':
                            # Se 'equipamento' for um int, copiar para a chave 'equipamentos' como lista
                            if isinstance(item.get('equipamento'), int):
                                item_corrigido['equipamentos'] = [item['equipamento']]
                            # Manter a chave 'equipamento' com o valor convertido
                            item_corrigido[coluna] = aplicar_transformacao(
                                item.get(coluna, 0), 
                                'int'
                            )
                        elif coluna == 'equipamentos':
                            # Se 'equipamentos' já existe no item, usar o valor convertido
                            if coluna in item:
                                item_corrigido[coluna] = aplicar_transformacao(
                                    item[coluna], 
                                    'list'
                                )
                            # Se não existe, já pode ter sido preenchido pela regra do 'equipamento'
                        else:
                            # Aplicar transformação conforme as regras do modelo
                            tratamento_erro = regras.get('tratamento_erro')
                            item_corrigido[coluna] = aplicar_transformacao(
                                item[coluna], 
                                regras['tipo'], 
                                tratamento_erro
                            )
                            
                            # Mensagem específica para erros de tempo
                            if coluna == 'tempo' and tratamento_erro == 'usar_zero':
                                try:
                                    # Tentar converter para verificar se haveria erro
                                    int(item[coluna])
                                except (ValueError, TypeError):
                                    print(f"Aviso: Item {i} - Valor de 'tempo' inválido: {item[coluna]}. Usando 0 como padrão.")
                                    
                    except ValueError as e:
                        erros.append(f"Item {i}: Erro ao converter '{coluna}': {str(e)}")
                        continue
                elif regras['obrigatorio']:
                    campos_faltantes.append(coluna)
            
            # Se houver campos obrigatórios faltando, registrar erro e pular item
            if campos_faltantes:
                for campo in campos_faltantes:
                    erros.append(f"Item {i}: Campo '{campo}' não encontrado")
                continue
            
            dados_corrigidos.append(item_corrigido)
            
        except Exception as e:
            erros.append(f"Item {i}: Erro ao processar - {str(e)}")
    
    if erros:
        print("\n⚠️  Erros encontrados durante a validação:")
        for erro in erros:
            print(f"  - {erro}")
    
    return dados_corrigidos

def analisar_tipagens(dados: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analisa as tipagens atuais dos dados e retorna um relatório.
    
    Args:
        dados: Lista de dicionários a serem analisados
        
    Returns:
        Dicionário com estatísticas das tipagens
    """
    analise = {
        'total_itens': len(dados),
        'tipagens_id_erp': {},
        'tipagens_codigo_barra': {},
        'tipagens_nome': {},
        'tipagens_tempo': {},
        'itens_com_campos_faltando': 0,
        'itens_com_tempo_zero': 0
    }
    
    for i, item in enumerate(dados):
        # Analisar id_erp
        if 'id_erp' in item:
            tipo = type(item['id_erp']).__name__
            analise['tipagens_id_erp'][tipo] = analise['tipagens_id_erp'].get(tipo, 0) + 1
            if item['id_erp'] == "" or item['id_erp'] is None:
                analise['itens_com_campos_faltando'] += 1
        
        # Analisar codigo_barra
        if 'codigo_barra' in item:
            tipo = type(item['codigo_barra']).__name__
            analise['tipagens_codigo_barra'][tipo] = analise['tipagens_codigo_barra'].get(tipo, 0) + 1
            if item['codigo_barra'] == "" or item['codigo_barra'] is None:
                analise['itens_com_campos_faltando'] += 1
        
        # Analisar nome
        if 'nome' in item:
            tipo = type(item['nome']).__name__
            analise['tipagens_nome'][tipo] = analise['tipagens_nome'].get(tipo, 0) + 1
            if item['nome'] == "" or item['nome'] is None:
                analise['itens_com_campos_faltando'] += 1
        
        # Analisar tempo
        if 'tempo' in item:
            tipo = type(item['tempo']).__name__
            analise['tipagens_tempo'][tipo] = analise['tipagens_tempo'].get(tipo, 0) + 1
            if item['tempo'] == 0:
                analise['itens_com_tempo_zero'] += 1
        
        # Verificar se algum campo está faltando
        campos_obrigatorios = ['id_erp', 'codigo_barra', 'nome', 'tempo']
        campos_faltantes = [campo for campo in campos_obrigatorios if campo not in item]
        if campos_faltantes:
            analise['itens_com_campos_faltando'] += 1
    
    return analise

def main():
    if len(sys.argv) < 2:
        print("Uso: python corrigir_tipagens.py <arquivo_entrada.json>")
        sys.exit(1)
    
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[1] + "_corrigido.json"
    
    try:
        # Ler o arquivo JSON
        print(f"📖 Lendo arquivo: {arquivo_entrada}")
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        # Validar se é uma lista
        if not isinstance(dados, list):
            print("❌ Erro: O arquivo JSON deve conter uma lista de objetos")
            sys.exit(1)
        
        print(f"✅ Arquivo lido com sucesso. Total de itens: {len(dados)}")
        
        # Análise inicial
        print("\n📊 Análise inicial das tipagens:")
        analise_inicial = analisar_tipagens(dados)
        print(json.dumps(analise_inicial, indent=2, ensure_ascii=False))
        
        # Processar e corrigir as tipagens
        print("\n🔧 Corrigindo tipagens...")
        dados_corrigidos = validar_e_corrigir_tipagem(dados)
        
        # Análise final
        print("\n📊 Análise após correção:")
        analise_final = analisar_tipagens(dados_corrigidos)
        print(json.dumps(analise_final, indent=2, ensure_ascii=False))
        
        # Salvar arquivo corrigido se caminho fornecido
        if arquivo_saida:
            print(f"\n💾 Salvando arquivo corrigido em: {arquivo_saida}")
            with open(arquivo_saida, 'w', encoding='utf-8') as f:
                json.dump(dados_corrigidos, f, ensure_ascii=False, indent=2)
            print("✅ Arquivo corrigido salvo com sucesso!")
        
        # Resumo final
        print(f"\n📋 Resumo:")
        print(f"   - Total de itens processados: {len(dados_corrigidos)}")
        print(f"   - Itens com campos vazios: {analise_final['itens_com_campos_faltando']}")
        print(f"   - Itens com tempo zero: {analise_final['itens_com_tempo_zero']}")
        
        return dados_corrigidos
        
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo não encontrado: {arquivo_entrada}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Erro: JSON inválido - {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
