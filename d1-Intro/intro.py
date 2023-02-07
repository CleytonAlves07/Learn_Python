# Iniciando python no terminal

# python3 nomeDoArquivo.py 
  # Pode ser utilizado a flag -i para continuar acessando e interagindo

#  Ao criar uma lista/array

trybe = ['Fundamentos']

# Para saber o tamanho da lista len() (mesmo que length em JS)

# Para incluir informações

trybe.append('Front-End')
trybe.append('Back-End')
trybe.append('CS')

# Para modificar um item da lista 

trybe[3] = 'Ciência da Computação'

print(trybe)

fruits = ["laranja", "maçã", "uva", "abacaxi"]  # elementos são definidos separados por vírgula, envolvidos por colchetes

fruits[0]  # o acesso é feito por índices iniciados em 0

fruits[-1]  # o acesso também pode ser negativo

fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("abacaxi")  # removendo uma fruta

fruits.extend(["pera", "melão", "kiwi"])  # acrescenta uma lista de frutas a lista original

fruits.index("maçã")  # retorna o índice onde a fruta está localizada, neste caso, 1

fruits.sort()  # ordena a lista de frutas
# Enumerando 
# enumerate_fruits = enumerate(fruits)

# print(enumerate_fruits)
# Um conjunto ou set(objeto) pode ser criado:
  # teste = set()
  # um conjunto não repete dados, mesmo que você inclua várias vezes, diferente da lista.
  # Um set não se importa com a ordem 

# permissions = {"member", "group"}  # elementos separados por vírgula, envolvidos por chaves

# permissions.add("root")  # adiciona um novo elemento ao conjunto

# permissions.add("member")  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

# permissions.union({"user"})  # retorna um conjunto resultado da união

# permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

# permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# permissions = frozenset(["member", "group"])  # assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset

# permissions.union({"user"})  # novos conjuntos imutáveis podem ser criados à partir do original, mas o mesmo não pode ser modificado

# permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

# permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# utilizando um loop de repetição 

ratings = [4, 8, 3, 7, 9, 10, 15]
# Colocando elementos em uma posição específica 
ratings.insert(4, 30)
print(ratings)
# Deletando em elemento em uma posição específica 
del ratings[3]
# remover um elemento específico 
ratings.remove(9)
most_recent_rating = ratings.pop(0)
print(ratings)
print(f'Most recent rating: {most_recent_rating}')

# Ordem aleatória 
ratings.sort()
print(f'Elementos em ordem aleatória: {ratings}')
new_ratings = []


for rating in ratings:
  new_ratings.append(rating * 10)
print(f'Old ratings: { ratings }; New ratings: { new_ratings }')

# Outra forma de fazer o for e mais comum é colocar já na lista o que pretende

outro_ratings = [ 10 * rating for rating in ratings ]

print(f'Outro ratings: { outro_ratings }')

# Uma função pode ser feita em python utilizando:

def biggest_name(names):
  big_name =  names[0]
  for name in names:
    if len(name) > len(big_name):
      big_name = name
  return print(f'O maior nome da lista é: {big_name}')

names = ["José", "Lucas", "Nádia", "Fernanda", "Borges", "Cairo", "Joana", "Francisgleydson", "Abel"]
biggest_name(names)

upper_case = [name.upper() for name in names]

print(f'Os nomes em caixa alta: {upper_case}')

# Ordem alfabética decrescente 
print(sorted(names, reverse=True))

# Para fazer um loop limitando até o número passado 

def asteristico(n):
  for row in range(n):
    print(n * '*')

asteristico(7)

# Para utilizar arredondamentos utilizando bibliotecas

import math

# Nessa função o usuário passa a área em m² que será pintada e o valor do galão de tinta e recebe. Quantas latas e o valor que será gasto.
def paint_cost(area, preco_lata):
  price = preco_lata
  liters = area / 3
  if liters < 18:
    required_gallon = 1
  required_gallon = math.ceil(liters / 18)
  return print(f'Gallon(s): {required_gallon}, Cost: {required_gallon * price}')

paint_cost(12, 125)

# Utilizando if/ elif/ else

def is_triangle(s1,s2,s3):
  triangle = (
    s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2
  )

  if not triangle:
    return print('Não é um triângulo')
  elif s1 == s2 == s3:
    return print('É um triângulo equilátero')
  elif s1 == s2 or s2 == s3 or s1 == s3:
    return print('É um triângulo isósceles')
  else:
    return print('É um trinângulo escaleno')

is_triangle(4, 4, 9)


def min(numbers):
  min_number = numbers[0]
  for number in numbers:
    if number < min_number:
      min_number = number
    if number < 0:
      return print('Jamaica abaixo de zero!')
  return print(f'O menor número é: { min_number }')

min([5, 9, 3, 19, 70, -8, 100, 2, 35, 27])

def minimo(numbers):
  return min(numbers)

minimo([5, 9, 3, 19, 70, 8, 100, 2, 35, 27])

def triangle_retangle(n):
  for number in range(1, n + 1):
    print(number * '*')

triangle_retangle(5)

def sum_all(n):
  all_sum = 0
  for number in range(1, n + 1): 
    all_sum += number
  print(all_sum)

sum_all(5)

# Pode ser utilizado com a função sum do Python

def somando(n):
  return print(sum(range(1, n +1)))

somando(10)

def combustivel(litros, tipo):
  price_g = 2.50
  price_a = 1.90
  if 'A' != tipo != 'G':
    print('Preencha o campo tipo com A para álcool ou G para Gasolina')
  if litros < 20 and tipo == 'A':
    total = price_a * 0.97 * litros
    print(f'Preço litro: R$ {price_a}\n Preço c/desconto: R$ {round(price_a * 0.97)}\n Total: { round(total, 2) }')
  elif litros < 20 and tipo == 'G':
    total = price_g * 0.96 * litros
    print(f'Preço litro: R$ {price_g}\n Preço c/desconto: R$ {round(price_g * 0.96)}\n Total: { round(total, 2) }')
  elif litros > 20 and tipo == 'A':
    total = price_a * 0.95 * litros
    print(f'Preço litro: R$ {price_a}\nPreço c/desconto: R$ {round(price_a * 0.95)}\nTotal: { round(total, 2) }')
  elif litros > 20 and tipo == 'G':
    total = price_g * 0.94 * litros
    print(f'Preço litro: R$ {price_g}\n Preço c/desconto: R$ {round(price_g * 0.94)}\n Total: { round(total, 2) }')
  
  
  

combustivel(35, 'G')

def fuel_price(type, liters):
    if type == "A":
        price = 1.90
        discount = 0.03
        if liters > 20:
            discount = 0.05
    elif type == "G":
        price = 2.50
        discount = 0.04
        if liters > 20:
            discount = 0.06
    total = price * liters
    total -= total * discount
    return total

# Entradas e saídas - dia 2

Name = input('Digite seu nome:  ')
for letter in Name:
  print(letter)

# Números grandes com underscore

faturamento = 1_000_000_000

print(faturamento)

# Formatar no formato da moeda brasileira 
  # Com vírgulas
print(f'O faturamento foi de R${faturamento:,}')
  # Com ponto 
text_faturamento = f'{faturamento:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')

  # Biblioteca para fazer isso 
import locale
# definir o local que você está
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # Portuguese_Brazil.1252

text_faturamento2 = locale.currency(faturamento, grouping=True)
print(f'O segundo faturamento foi de {text_faturamento2}')

# Fazer um if simples na mesma linha

fatu = 400

bonus = 200 if fatu > 500 else 50

print(f'Bônus: {bonus}')

# list comprehension

lista_produtos = ['celular', 'tablet', 'fone de ouvido', 'camera', 'microfone']
lista_precos = [1000, 1200, 300, 500, 600]
# Pegando os dois primeiros da lista produtos
first_two = lista_produtos[:2]
remove_last = lista_produtos[:-1]
print(f'Pegando os dois primeiros da lista produtos: {first_two}')
preco_reajustado=[preco * 1.1 for preco in lista_precos]

print(preco_reajustado)


# Unpacking
# a lista forma uma tupla
lista_produtos = [
 ('celular', 1000),
 ('tablet', 1200),
 ('fone de ouvido', 300),
 ('camera', 500),
 ('microfone', 600)
]
# Podemos pegar os itens da tupla e nomea-los.
for produto,preco in lista_produtos:
  print(f'O produto {produto} for reajustado de {preco} para R$ {preco * 1.1}')


copy_of_list_produtos = lista_produtos[:]
print(f'Copy: {copy_of_list_produtos}')

alien = {'color': 'green', 'points': 5}
# Add
alien['position'] = 0

print('The alien color is ' + alien['color'])
print(alien)

favorite_num = {'eric': 17, 'ever': 4}
# Forma de pegar os items de um conjunto
for name, number in favorite_num.items():
  print(name + ' loves ' + str(number))

# Forma de pegar a chave - key
for name in favorite_num.keys():
  print(name + ' loves a number')

# Forma de pegar o valor 
for number in favorite_num.values():
  print(str(number) + ' is a favorite')

# While loops

current = 1
while current <= 5:
  print(f'O valor corrente é {current}')
  current += 1

msg = ''
while msg != 'quit':
  msg = input('What is your message?')
  if msg == 'quit':
    print('Acertô miseravi!')
  else:
    print('Você tem que escrever quit para sair desse programa')

# Estabelecendo um valor por default em uma função

def make_pizza(topping='bacon'):
  print(f'Have a {topping} pizza!')

make_pizza()
make_pizza('calabresa')


# List comprehensions - de 0 a 10
squares = [x**2 for x in range(11)]
print(f'Squares: {squares}')

# Imprimindo um dicionário em uma lista
new_client = {
  'last': 'Alves',
  'first': 'Cleyton',
  'username': 'Alves2'
}
other_client = {
  'last': 'Silva',
  'first': 'Roberto',
  'username': 'Robão'
}
clients = []
clients.append(new_client)
clients.append(other_client)

for client_dic in clients:
  for prop, attrib in client_dic.items():
    print(prop + ':  ' + attrib)
  print('\n')

# lista dentro de um dicionário
fav_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, langs in fav_languages.items():
  print(f'{name}: ')
  for lang in langs:
    print(f'- {lang}')

