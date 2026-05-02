import requests
import json
import os

### VARIABLES ###
URL_ORIGEM = ""
URL_DESTINO = "http://10.147.18.168"
FAZER_PUT = False  # Mude para False para apenas ler os dados e não fazer PUT no destino
PASTA_BACKUP = "bkp_permobili"  # Pasta onde são salvos/lidos os arquivos JSON
MODO = "restore"  # "backup" para buscar da origem e salvar | "restore" para ler da pasta e enviar PUT

def fetch_json(url, id):
    try:
        response = requests.get(f'{url}:{3030+id}/equipamento/config')
        response.raise_for_status()  # Raise an error for bad status codes
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def fetch_equipamentos():
    try:
        response = requests.get(f"{URL_ORIGEM}:3000/octopus/")
        response.raise_for_status()
        
        # Obtém o JSON - parece ser um objeto com chaves, não uma lista
        data = response.json()

        # Cria uma array com os _id dos equipamentos
        ids_equipamentos = []
        
        # Se a resposta for um dicionário, procuramos pela chave 'equipamentos'
        if isinstance(data, dict):
            # Verifica se existe a chave 'equipamentos'
            if 'equipamentos' in data:
                equipamentos = data['equipamentos']
                
                # Itera sobre cada equipamento na lista
                for equipamento in (equipamentos):                    
                    if isinstance(equipamento, dict):
                        # Extrai o _id se existir
                        if '_id' in equipamento:
                            id_equipamento = equipamento['_id']
                            ids_equipamentos.append(id_equipamento)
                        else:
                            print("  _id não encontrado neste equipamento")
                            # Mostra chaves alternativas que podem conter ID
                            chaves_possiveis = [k for k in equipamento.keys() if 'id' in k.lower()]
                            if chaves_possiveis:
                                print(f"  Chaves alternativas com ID: {chaves_possiveis}")
                        
                    else:
                        print(f"  Conteúdo: {equipamento}")
                    
            else:
                print("\nChave 'equipamentos' não encontrada na resposta!")
                print("Conteúdo da resposta:")
                print(data)
        else:
            print("A resposta não é um dicionário como esperado!")
        
        return data, ids_equipamentos
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching equipamentos: {e}")
        return None, []

def restaurar_backup():
    """Lê os arquivos JSON da pasta de backup e faz PUT para o destino"""
    contar = 0
    ids_processados = []
    equipamentos_com_erro = []
    
    print(f"\n{'='*60}")
    print(f"🔄 MODO RESTAURAÇÃO")
    print(f"{'='*60}\n")
    
    try:
        # Verifica se a pasta existe
        if not os.path.exists(PASTA_BACKUP):
            print(f"❌ Pasta '{PASTA_BACKUP}' não encontrada!")
            return
        
        # Lista todos os arquivos na pasta
        arquivos = os.listdir(PASTA_BACKUP)
        
        # Filtra apenas arquivos .json que começam com 'config_port'
        arquivos_json = [f for f in arquivos if f.startswith('config_port') and f.endswith('.json')]
        
        print(f"📂 Encontrados {len(arquivos_json)} arquivos JSON na pasta '{PASTA_BACKUP}'")
        print(f"📍 URL de destino: {URL_DESTINO}\n")
        
        if not arquivos_json:
            print("⚠️  Nenhum arquivo config_port_*.json encontrado!\n")
            return
        
        for arquivo in arquivos_json:
            caminho_completo = os.path.join(PASTA_BACKUP, arquivo)
            
            try:
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                
                # Extrai o _id dos dados
                if '_id' in dados:
                    id_eqp = dados['_id']
                    
                    print(f"📋 Processando: {arquivo} (ID: {id_eqp})")
                    
                    # Constrói a URL para o PUT
                    url = f"{URL_DESTINO}:{3030+id_eqp}/equipamento/config"
                    
                    payload = {
                        "data": dados
                    }
                    
                    try:
                        response = requests.put(
                            url,
                            json=payload,
                            headers={"Content-Type": "application/json"},
                            timeout=5
                        )
                        response.raise_for_status()
                        print(f"✅ Dados enviados com sucesso para {url}")
                        contar += 1
                        ids_processados.append(id_eqp)
                    except requests.exceptions.RequestException as e:
                        print(f"❌ Erro ao enviar dados para {url}: {type(e).__name__}")
                        equipamentos_com_erro.append({
                            "id": id_eqp,
                            "nome_equipamento": dados.get('nome', 'Desconhecido'),
                            "erro": str(e),
                            "arquivo": arquivo
                        })
                else:
                    print(f"⚠️  Arquivo {arquivo} não contém campo '_id'\n")
                    
            except json.JSONDecodeError as e:
                print(f"❌ Erro ao ler JSON do arquivo {arquivo}: {e}")
            except Exception as e:
                print(f"❌ Erro ao processar arquivo {arquivo}: {type(e).__name__}: {str(e)}")
        
    except Exception as e:
        print(f"❌ Erro ao acessar pasta '{PASTA_BACKUP}': {type(e).__name__}: {str(e)}")
        return
    
    # Imprime resumo final
    print("\n" + "="*60)
    print(f"Fim da restauração: {contar} arquivo(s) processado(s) com sucesso.")
    print(f"📂 Pasta de origem: {PASTA_BACKUP}")
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

def main():
    # Busca a lista de equipamentos e seus IDs
    _, ids_equipamentos = fetch_equipamentos()
    contar = 0
    ids_processados = []
    equipamentos_com_erro = []
    
    # Cria a pasta de backup se não existir
    if not os.path.exists(PASTA_BACKUP):
        os.makedirs(PASTA_BACKUP)
        print(f"📁 Pasta de backup criada: {PASTA_BACKUP}\n")
    else:
        print(f"📁 Pasta de backup já existe: {PASTA_BACKUP}\n")
    
    # Itera sobre cada ID de equipamento
    for id_eqp in ids_equipamentos:
        try:
            data = fetch_json(URL_ORIGEM, id_eqp)
            if data is not None:
                print("Data fetched successfully:")
                
                # Salva os dados em arquivo JSON separado para cada equipamento na pasta de backup
                nome_arquivo = f"config_port_{3030+id_eqp}.json"
                caminho_arquivo = os.path.join(PASTA_BACKUP, nome_arquivo)
                with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"✅ Dados salvos em: {caminho_arquivo}")
                
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
                        contar += 1
                        ids_processados.append(id_eqp)
                    except requests.exceptions.RequestException as e:
                        print(f"\n❌ Erro ao enviar dados para equipamento {id_eqp}: {type(e).__name__}")
                        equipamentos_com_erro.append({
                            "id": id_eqp,
                            "nome_equipamento": data.get('nome', 'Desconhecido'),
                            "erro": str(e)
                        })
                else:
                    # Modo leitura apenas - não faz PUT
                    print(f"Modo leitura apenas: dados do equipamento {id_eqp} não foram enviados (PUT desativado)")
                    contar += 1
                    ids_processados.append(id_eqp)
            else:
                print(f"\n❌ Falha ao buscar dados do equipamento {id_eqp}")
                equipamentos_com_erro.append({
                    "id": id_eqp,
                    "nome_equipamento": "Desconhecido",
                    "erro": "Falha ao buscar dados"
                })
        except Exception as e:
            print(f"\n❌ Erro inesperado no equipamento {id_eqp}: {type(e).__name__}: {str(e)}")
            equipamentos_com_erro.append({
                "id": id_eqp,
                "nome_equipamento": "Desconhecido",
                "erro": f"{type(e).__name__}: {str(e)}"
            })
    
    # Imprime resumo final
    print("\n" + "="*60)
    print(f"Fim do script: {contar} equipamentos processados com sucesso.")
    print(f"✅ Dados de {len(ids_processados)} equipamentos salvos em arquivos JSON separados")
    print(f"📍 URL de origem: {URL_ORIGEM}")
    print(f"📁 Pasta de backup: {PASTA_BACKUP}")
    print("="*60)
    
    # Imprime equipamentos com erro
    if equipamentos_com_erro:
        print(f"\n⚠️  {len(equipamentos_com_erro)} equipamento(s) com erro:\n")
        for idx, erro_info in enumerate(equipamentos_com_erro, 1):
            print(f"{idx}. ID: {erro_info['id']} | Nome: {erro_info['nome_equipamento']}")
            print(f"   Erro: {erro_info['erro']}\n")
    else:
        print("\n✅ Nenhum equipamento com erro!")

if __name__ == "__main__":
    print("="*60)
    print("📦 SCRIPT DE BACKUP E RESTAURAÇÃO PROMETHEUS")
    print("="*60)
    print("\nSelecione o modo de operação:")
    print("  1 - Backup: buscar da origem e salvar em arquivos JSON")
    print("  2 - Restore: ler arquivos JSON e enviar PUT para destino")
    print("="*60)
    
    escolha = input("\nDigite sua escolha (1 ou 2): ").strip()
    
    if escolha == "2":
        # Modo restauração: lê arquivos da pasta e envia PUT para destino
        if not URL_DESTINO:
            print("❌ URL_DESTINO não configurado! Configure para fazer restauração.")
            print("   Exemplo: URL_DESTINO = 'http://10.147.18.231'")
        else:
            restaurar_backup()
    else:
        # Modo backup: busca da origem e salva em arquivos
        main()
