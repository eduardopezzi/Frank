import os
import json
import requests

### VARIABLES ###
URL_DESTINO = "http://10.147.18.231"
FAZER_PUT = True  # Mude para False para apenas ler os dados e não fazer PUT no destino
PASTA_ARQUIVOS = "bkp_permobili"  # Pasta onde estão os arquivos JSON de backup

def ler_arquivos_json():
    """Lê todos os arquivos JSON da pasta de backup e retorna lista com dados"""
    dados_arquivos = []
    
    try:
        # Lista todos os arquivos na pasta
        arquivos = os.listdir(PASTA_ARQUIVOS)
        
        # Filtra apenas arquivos .json que começam com 'config_port'
        arquivos_json = [f for f in arquivos if f.startswith('config_port') and f.endswith('.json')]
        
        print(f"\n📂 Encontrados {len(arquivos_json)} arquivos JSON na pasta '{PASTA_ARQUIVOS}'\n")
        
        for arquivo in arquivos_json:
            caminho_completo = os.path.join(PASTA_ARQUIVOS, arquivo)
            
            try:
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                
                # Extrai o _id dos dados
                if '_id' in dados:
                    id_equipamento = dados['_id']
                    
                    dados_arquivos.append({
                        "id": id_equipamento,
                        "dados": dados,
                        "nome_arquivo": arquivo
                    })
                    
                    print(f"✅ Arquivo lido: {arquivo} (ID: {id_equipamento})")
                else:
                    print(f"⚠️  Arquivo {arquivo} não contém campo '_id'")
                    
            except json.JSONDecodeError as e:
                print(f"❌ Erro ao ler JSON do arquivo {arquivo}: {e}")
            except Exception as e:
                print(f"❌ Erro ao processar arquivo {arquivo}: {e}")
        
        return dados_arquivos
        
    except FileNotFoundError:
        print(f"❌ Pasta '{PASTA_ARQUIVOS}' não encontrada!")
        return []
    except Exception as e:
        print(f"❌ Erro ao acessar pasta '{PASTA_ARQUIVOS}': {e}")
        return []

def main():
    # Lê os arquivos JSON da pasta de backup
    dados_arquivos = ler_arquivos_json()
    contar = 0
    ids_processados = []
    equipamentos_com_erro = []
    dados_salvos = []  # Armazena os dados lidos dos arquivos
    
    # Itera sobre cada arquivo lido
    for item in dados_arquivos:
        id_eqp = item['id']
        data = item['dados']
        nome_arquivo = item['nome_arquivo']
        
        try:
            print(f"\n📋 Processando: {nome_arquivo} (ID: {id_eqp})")
            
            # Salva os dados lidos
            dados_salvos.append({
                "id": id_eqp,
                "dados": data,
                "nome_arquivo": nome_arquivo
            })
            
            if FAZER_PUT:
                url = f"{URL_DESTINO}:{3030+id_eqp}/equipamento/config"

                payload = {
                    "data": data
                }

                try:
                    requests.put(
                        url,
                        json=payload,              # envia JSON
                        headers={"Content-Type": "application/json"},
                        timeout=5
                    )
                    print(f"✅ Dados enviados com sucesso para ID {id_eqp}")
                    contar += 1
                    ids_processados.append(id_eqp)
                except requests.exceptions.RequestException as e:
                    print(f"\n❌ Erro ao enviar dados para equipamento {id_eqp}: {type(e).__name__}")
                    equipamentos_com_erro.append({
                        "id": id_eqp,
                        "nome_equipamento": data.get('nome', 'Desconhecido'),
                        "erro": str(e),
                        "arquivo": nome_arquivo
                    })
            else:
                # Modo leitura apenas - não faz PUT
                print(f"📖 Modo leitura apenas: dados do arquivo {nome_arquivo} não foram enviados (PUT desativado)")
                contar += 1
                ids_processados.append(id_eqp)
                
        except Exception as e:
            print(f"\n❌ Erro inesperado ao processar {nome_arquivo}: {type(e).__name__}: {str(e)}")
            equipamentos_com_erro.append({
                "id": id_eqp,
                "nome_equipamento": data.get('nome', 'Desconhecido') if data else 'Desconhecido',
                "erro": f"{type(e).__name__}: {str(e)}",
                "arquivo": nome_arquivo
            })
    
    # Salvar dados lidos em arquivo txt
    if dados_salvos:
        with open('dados_fetch.txt', 'w', encoding='utf-8') as f:
            for item in dados_salvos:
                f.write(f"ID: {item['id']}\n")
                f.write(f"Arquivo: {item['nome_arquivo']}\n")
                f.write(f"dados: {item['dados']}\n")
                f.write("-" * 60 + "\n")
        print(f"\n✅ Dados de {len(dados_salvos)} arquivos salvos em 'dados_fetch.txt'")
    
    # Imprime resumo final
    print("\n" + "="*60)
    print(f"Fim do script: {contar} arquivo(s) processado(s) com sucesso.")
    print(f"📂 Pasta de origem dos arquivos: {PASTA_ARQUIVOS}")
    print(f"📍 URL de destino: {URL_DESTINO}")
    print("="*60)
    
    # Imprime equipamentos com erro
    if equipamentos_com_erro:
        print(f"\n⚠️  {len(equipamentos_com_erro)} arquivo(s) com erro:\n")
        for idx, erro_info in enumerate(equipamentos_com_erro, 1):
            print(f"{idx}. ID: {erro_info['id']} | Nome: {erro_info['nome_equipamento']} | Arquivo: {erro_info.get('arquivo', 'N/A')}")
            print(f"   Erro: {erro_info['erro']}\n")
    else:
        print("\n✅ Nenhum arquivo com erro!")

if __name__ == "__main__":
    main()   # 👈 só essa roda
