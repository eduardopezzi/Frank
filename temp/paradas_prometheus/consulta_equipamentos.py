#!/usr/bin/env python3
"""
Script para consultar configurações de equipamentos via HTTP
"""

import requests
import json
import os
from typing import Dict, Any, Optional, List

# Configurações
IP_ORIGEM = "idimex"  # Altere para o IP correto
PORTA_BASE = 3030
TIMEOUT = 5  # segundos
ARQUIVO_SAIDA_CONFIG = "equipamentos_config.txt"
ARQUIVO_SAIDA_FATOR = "equipamentos_fator.txt"


def consultar_equipamento(ip: str, porta: int) -> Optional[Dict[str, Any]]:
    """
    Faz uma requisição GET para obter a configuração do equipamento
    
    Args:
        ip: Endereço IP do equipamento
        porta: Porta do equipamento
        
    Returns:
        Dicionário com os dados do equipamento ou None se falhar
    """
    url = f"http://{ip}:{porta}/equipamento/config/"
    
    try:
        response = requests.get(url, timeout=TIMEOUT)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"  ❌ Erro HTTP {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print(f"  ⏱️ Timeout - não respondeu em {TIMEOUT}s")
        return None
    except requests.exceptions.ConnectionError:
        print(f"  🔌 Erro de conexão")
        return None
    except json.JSONDecodeError:
        print(f"  📄 Resposta não é JSON válido")
        return None
    except Exception as e:
        print(f"  ⚠️ Erro inesperado: {e}")
        return None


def extrair_dados_equipamento(dados: Dict[str, Any]) -> Dict[str, str]:
    """
    Extrai os campos id, nome e parada_automatica da resposta
    
    Args:
        dados: Dicionário com a resposta JSON
        
    Returns:
        Dicionário com os campos extraídos
    """
    return {
        'id': str(dados.get('id', 'N/A')),
        'nome': str(dados.get('nome', 'N/A')),
        'parada_automatica': str(dados.get('parada_automatica', 'N/A'))
    }


def salvar_equipamento(arquivo, dados: Dict[str, str], numero_eqp: int) -> None:
    """
    Salva os dados do equipamento no arquivo de saída
    
    Args:
        arquivo: Arquivo aberto para escrita
        dados: Dicionário com os dados do equipamento
        numero_eqp: Número do equipamento
    """
    linha = f"{numero_eqp}|{dados['nome']}|{dados['parada_automatica']}"
    arquivo.write(linha + '\n')


def consultar_equipamento_fatores(ip: str, porta: int) -> Optional[Dict[str, Any]]:
    """
    Faz uma requisição GET para obter os dados do equipamento (endpoint /equipamento/)
    
    Args:
        ip: Endereço IP do equipamento
        porta: Porta do equipamento
        
    Returns:
        Dicionário com os dados do equipamento ou None se falhar
    """
    url = f"http://{ip}:{porta}/equipamento/"
    
    try:
        response = requests.get(url, timeout=TIMEOUT)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"  ❌ Erro HTTP {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print(f"  ⏱️ Timeout - não respondeu em {TIMEOUT}s")
        return None
    except requests.exceptions.ConnectionError:
        print(f"  🔌 Erro de conexão")
        return None
    except json.JSONDecodeError:
        print(f"  📄 Resposta não é JSON válido")
        return None
    except Exception as e:
        print(f"  ⚠️ Erro inesperado: {e}")
        return None


def extrair_fatores(dados: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extrai os fatores dos dados do equipamento
    
    Args:
        dados: Dicionário com a resposta JSON do endpoint /equipamento/
        
    Returns:
        Lista de dicionários contendo os fatores
    """
    fatores_list = dados.get('fator', [])
    resultado = []
    
    for idx, fator_row in enumerate(fatores_list):
        if isinstance(fator_row, list):
            for fator in fator_row:
                resultado.append({
                    'posicao': idx,
                    'fator': fator
                })
    
    return resultado


def gerar_nome_arquivo_unico(nome_base: str, extensao: str = '.txt') -> str:
    """
    Gera um nome de arquivo único, adicionando numeração se necessário
    
    Args:
        nome_base: Nome base do arquivo (sem extensão)
        extensao: Extensão do arquivo (default: .txt)
        
    Returns:
        Nome do arquivo único
    """
    nome_arquivo = nome_base + extensao
    
    # Verifica se o arquivo já existe
    contador = 1
    while os.path.exists(nome_arquivo):
        nome_arquivo = f"{nome_base}_{contador}{extensao}"
        contador += 1
    
    return nome_arquivo


def salvar_fatores(arquivo, dados_equipamento: Dict[str, Any], fatores: List[Dict[str, Any]], numero_eqp: int) -> None:
    """
    Salva os dados do equipamento e seus fatores no arquivo de saída
    
    Args:
        arquivo: Arquivo aberto para escrita
        dados_equipamento: Dados completos do equipamento
        fatores: Lista de fatores extraídos
        numero_eqp: Número do equipamento
    """
    nome = dados_equipamento.get('nome', 'N/A')
    _id = dados_equipamento.get('_id', 'N/A')
    
    # Escreve cabeçalho do equipamento
    arquivo.write(f"\n{'=' * 60}\n")
    arquivo.write(f"Equipamento {numero_eqp}: {nome} (ID: {_id})\n")
    arquivo.write(f"{'=' * 60}\n")
    
    # Escreve os fatores
    if fatores:
        arquivo.write(f"Total de fatores: {len(fatores)}\n")
        arquivo.write(f"{'Posição':<15} {'Fator':<10}\n")
        arquivo.write(f"{'-' * 30}\n")
        for fator in fatores:
            arquivo.write(f"{fator['posicao']:<15} {fator['fator']:<10}\n")
    else:
        arquivo.write("Nenhum fator encontrado\n")


def consultar_configuracoes(qtd_equipamentos: int) -> None:
    """
    Consulta as configurações dos equipamentos (endpoint /equipamento/config/)
    
    Args:
        qtd_equipamentos: Quantidade de equipamentos para consultar
    """
    print(f"\nConsultando {qtd_equipamentos} equipamento(s)...")
    print("-" * 60)
    
    equipamentos_com_sucesso = 0
    equipamentos_falharam = 0
    
    # Abre arquivo para escrita
    with open(ARQUIVO_SAIDA_CONFIG, 'w', encoding='utf-8') as arquivo:
        # Escreve cabeçalho
        arquivo.write("ID|Nome|Parada_Automatica\n")
        
        # Faz requisição para cada equipamento
        for i in range(1, qtd_equipamentos + 1):
            porta = PORTA_BASE + i
            print(f"Equipamento {i} (porta {porta}): ", end='', flush=True)
            
            # Consulta equipamento
            dados_json = consultar_equipamento(IP_ORIGEM, porta)
            
            if dados_json:
                # Extrai dados relevantes
                dados = extrair_dados_equipamento(dados_json)
                
                # Salva no arquivo
                salvar_equipamento(arquivo, dados, i)
                
                print(f"✅ Sucesso - ID: {dados['id']}, Nome: {dados['nome']}")
                equipamentos_com_sucesso += 1
            else:
                print(f"❌ Falha na consulta")
                equipamentos_falharam += 1
    
    # Resumo
    print("-" * 60)
    print(f"\n✅ Consultas bem-sucedidas: {equipamentos_com_sucesso}")
    print(f"❌ Consultas falharam: {equipamentos_falharam}")
    print(f"\n📄 Resultados salvos em: {ARQUIVO_SAIDA_CONFIG}")
    print("=" * 60)


def consultar_fatores(qtd_equipamentos: int) -> None:
    """
    Consulta os fatores dos equipamentos (endpoint /equipamento/)
    
    Args:
        qtd_equipamentos: Quantidade de equipamentos para consultar
    """
    print(f"\nConsultando {qtd_equipamentos} equipamento(s)...")
    print("-" * 60)
    
    equipamentos_com_sucesso = 0
    equipamentos_falharam = 0
    
    # Gera nome único para o arquivo
    nome_arquivo = gerar_nome_arquivo_unico(ARQUIVO_SAIDA_FATOR.replace('.txt', ''))
    
    # Abre arquivo para escrita
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        # Escreve cabeçalho geral
        arquivo.write("=" * 60 + "\n")
        arquivo.write("RELATÓRIO DE FATORES DE EQUIPAMENTOS\n")
        arquivo.write("=" * 60 + "\n")
        arquivo.write(f"IP Origem: {IP_ORIGEM}\n")
        arquivo.write(f"Porta Base: {PORTA_BASE}\n")
        arquivo.write(f"Data: {__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        
        # Faz requisição para cada equipamento
        for i in range(1, qtd_equipamentos + 1):
            porta = PORTA_BASE + i
            print(f"Equipamento {i} (porta {porta}): ", end='', flush=True)
            
            # Consulta equipamento
            dados_json = consultar_equipamento_fatores(IP_ORIGEM, porta)
            
            if dados_json:
                # Extrai fatores
                fatores = extrair_fatores(dados_json)
                
                # Salva no arquivo
                salvar_fatores(arquivo, dados_json, fatores, i)
                
                print(f"✅ Sucesso - Nome: {dados_json.get('nome', 'N/A')}, Fatores: {len(fatores)}")
                equipamentos_com_sucesso += 1
            else:
                print(f"❌ Falha na consulta")
                equipamentos_falharam += 1
    
    # Resumo
    print("-" * 60)
    print(f"\n✅ Consultas bem-sucedidas: {equipamentos_com_sucesso}")
    print(f"❌ Consultas falharam: {equipamentos_falharam}")
    print(f"\n📄 Resultados salvos em: {nome_arquivo}")
    print("=" * 60)


def main():
    """
    Função principal do programa
    """
    print("=" * 60)
    print("Consulta de Equipamentos via HTTP")
    print("=" * 60)
    print(f"IP Origem: {IP_ORIGEM}")
    print(f"Porta Base: {PORTA_BASE}")
    print()
    
    # Menu de opções
    print("Escolha o tipo de consulta:")
    print("  1 - Consultar configurações (endpoint /equipamento/config/)")
    print("  2 - Consultar fatores (endpoint /equipamento/)")
    print()
    
    try:
        opcao = int(input("Informe a opção desejada (1 ou 2): "))
        if opcao not in [1, 2]:
            print("❌ Opção inválida! Escolha 1 ou 2.")
            return
    except ValueError:
        print("❌ Por favor, informe um número válido!")
        return
    
    # Solicita quantidade de equipamentos
    try:
        qtd_equipamentos = int(input("\nInforme a quantidade de equipamentos: "))
        if qtd_equipamentos <= 0:
            print("❌ Quantidade deve ser maior que zero!")
            return
    except ValueError:
        print("❌ Por favor, informe um número válido!")
        return
    
    # Executa a consulta escolhida
    if opcao == 1:
        consultar_configuracoes(qtd_equipamentos)
    else:
        consultar_fatores(qtd_equipamentos)


if __name__ == "__main__":
    main()
