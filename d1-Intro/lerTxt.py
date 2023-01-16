file = 'pythontxt.txt'

# Para escrever - escreve por cima do conteúdo que já existir
with open(file, 'w') as file_object:
  file_object.write('Se você está lendo isso, é melhor voltar para o último commit')

# Para anexar algo
with open(file, 'a') as file_object:
  file_object.write('Espero aprender mais sobre automação, Machine Learn e IA')

# Para ler 
with open(file) as file_object:
  lines = file_object.readlines()

for line in lines:
  print(line)

