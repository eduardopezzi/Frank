# Consulta de Equipamentos via HTTP

Programa Python para consultar configurações de múltiplos equipamentos via requisições HTTP GET.

## Funcionalidades

- Faz requisições GET para múltiplos equipamentos
- Extrai os campos: `id`, `nome` e `parada_automatica`
- Salva os resultados em um arquivo texto
- Trata erros de conexão, timeout e respostas inválidas
- Exibe relatório de sucesso/falha

## Configuração

Antes de executar, edite o arquivo `consulta_equipamentos.py` e altere as configurações na seção superior:

```python
IP_ORIGEM = "192.168.1.1"  # Altere para o IP correto
PORTA_BASE = 3030          # Porta base (3030 + ID_EQP)
TIMEOUT = 5                # Timeout em segundos
ARQUIVO_SAIDA = "equipamentos.txt"  # Nome do arquivo de saída
```

## Instalação

O programa requer a biblioteca `requests`. Instale com:

```bash
pip install -r requirements.txt
```

## Execução

Execute o programa e informe a quantidade de equipamentos:

```bash
python3 consulta_equipamentos.py
```

Exemplo de execução:
```
============================================================
Consulta de Equipamentos via HTTP
============================================================
IP Origem: 192.168.1.1
Porta Base: 3030

Informe a quantidade de equipamentos: 3

Consultando 3 equipamento(s)...
------------------------------------------------------------
Equipamento 1 (porta 3031): ✅ Sucesso - ID: 1, Nome: Equipamento A
Equipamento 2 (porta 3032): ✅ Sucesso - ID: 2, Nome: Equipamento B
Equipamento 3 (porta 3033): ❌ Falha na consulta
------------------------------------------------------------

✅ Consultas bem-sucedidas: 2
❌ Consultas falharam: 1

📄 Resultados salvos em: equipamentos.txt
============================================================
```

## Formato da URL

Para cada equipamento, o programa constrói a URL da seguinte forma:

```
http://{IP_ORIGEM}:{PORTA_BASE + ID_EQP}/equipamento/config/
```

Exemplos:
- Equipamento 1: `http://192.168.1.1:3031/equipamento/config/`
- Equipamento 2: `http://192.168.1.1:3032/equipamento/config/`
- Equipamento 3: `http://192.168.1.1:3033/equipamento/config/`

## Formato do Arquivo de Saída

O arquivo `equipamentos.txt` conterá:

```
ID|Nome|Parada_Automatica
1|Equipamento A|true
2|Equipamento B|false
```

## Tratamento de Erros

O programa trata os seguintes erros:
- **Timeout**: Equipamento não responde dentro do tempo limite
- **ConnectionError**: Equipamento não alcançável
- **HTTP Error**: Resposta com código diferente de 200
- **JSONDecodeError**: Resposta não é um JSON válido

Equipamentos com erro são ignorados e o programa continua com os próximos.