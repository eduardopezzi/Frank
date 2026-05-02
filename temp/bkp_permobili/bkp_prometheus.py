import requests

### VARIABLES ###
URL_ORIGEM = "http://10.147.18.168"
URL_DESTINO = ""
FAZER_PUT = False  # Mude para False para apenas ler os dados e não fazer PUT no destino

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

def main():
    # Busca a lista de equipamentos e seus IDs
    _, ids_equipamentos = fetch_equipamentos()
    contar = 0
    ids_processados = []
    equipamentos_com_erro = []
    dados_salvos = []  # Armazena os dados retornados pelo fetch
    
    # Itera sobre cada ID de equipamento
    for id_eqp in ids_equipamentos:
        try:
            data = fetch_json(URL_ORIGEM, id_eqp)
            if data is not None:
                print("Data fetched successfully:")
                
                # Salva os dados retornados
                dados_salvos.append({
                    "id": id_eqp,
                    "dados": data
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
    
    # Salvar dados do fetch em arquivo txt
    if dados_salvos:
        with open('dados_fetch.txt', 'w') as f:
            for item in dados_salvos:
                f.write(f"ID: {item['id']}\n")
                f.write(f"dados: {item['dados']}\n")
                f.write("-" * 60 + "\n")
        print(f"\n✅ Dados de {len(dados_salvos)} equipamentos salvos em 'dados_fetch.txt'")
    
    # Imprime resumo final
    print("\n" + "="*60)
    print(f"Fim do script: {contar} equipamentos processados com sucesso.")
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
    main()   # 👈 só essa roda
