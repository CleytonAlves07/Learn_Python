# Para ler arquivos json em python

import json
import requests

# Fazendo uma requisição
request_cotacao = requests.get(
    'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = request_cotacao.json()

# Utilizando as chaves dentro do json
cotacao_bid_BTCBRL = cotacao['BTCBRL']['bid']
cotacao_ask_BTCBRL = cotacao['BTCBRL']['ask']
cotacao_name_BTCBRL = cotacao['BTCBRL']['name']
nome = cotacao_name_BTCBRL.split('/')

print(f'A  moeda { nome[1] } está com o preço de venda de  R$ { cotacao_ask_BTCBRL } e o preço de compra de R$ { cotacao_bid_BTCBRL }')


# file = open('arquivojson.json', 'r')
# mercado_livre = json.load(file)
# file.close()

# Utilizando o with não é necessário fechar. Se estiver fora do with ele já fecha
def main():
    try:
        with open('cotacao.json', 'r') as file:
            cotacao = json.load(file)
    except FileNotFoundError as exc:
        # raise FileNotFoundError('Arquivo ou caminho inexistente!')
        print('Arquivo ou caminho inexistente!')
    except json.decoder.JSONDecodeError as exc:
        print('Arquivo com formato errado')


# Com esse if a abertura do arquivo só irá acontecer quando a função main for chamada
if __name__ == '__main__':
    main()
