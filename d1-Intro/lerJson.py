# Para ler arquivos json em python

import json
import requests

request_cotacao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
print(request_cotacao.json())

# file = open('arquivojson.json', 'r')
# mercado_livre = json.load(file)
# file.close()

# Utilizando o with não é necessário fechar. Se estiver fora do with ele já fecha
def main():
  try:
    with open('cotacao.json', 'r') as file:
      cotacao = json.load(file)
  except FileNotFoundError as exc:
    print('Arquivo inexistente!')
  except json.decoder.JSONDecodeError as exc:
    print('Arquivo inexistente')


if __name__ == '__main__':
  main()
