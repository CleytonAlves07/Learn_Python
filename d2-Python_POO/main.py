from personagem import Personagem
from jedi_sith import Jedi, Sith

# Criando um personagem (objeto da classe)

personagem_Frodo = Personagem('Frodo', 'Hobbit', 120)

print(f'O nome do personagem é { personagem_Frodo.nome }')

# Utilizando o método get
print(f'O hp dele é de { personagem_Frodo.get_hp()} - Método get')

# Utilizando property
print(f'O hp dele é de { personagem_Frodo.hp} - Acessando via property')

# O vars mostra um dicionário com todos as propriedades e os atributos 
# Ex: {'nome': 'Frodo', 'raca': 'Hobbit', 'hp': 120}

print(vars(personagem_Frodo))

# método set
personagem_Frodo.set_hp(95)
print(f'O life do personagem { personagem_Frodo.nome } agora é de { personagem_Frodo.hp }')

# método setter decorador
personagem_Frodo.hp = 5
print(f'O life do personagem { personagem_Frodo.nome } agora é de { personagem_Frodo.hp } - utilizando o método setter')


personagem_Obi = Jedi('Obi Wan', 'Humano', 2000)
personagem_Darth = Sith('Darth Maul', 'Dathomirian', 1800)

print('---------------------------')
print('Batalha')
print(f'{personagem_Darth.nome}: {personagem_Darth.falar()}')
print(f'{personagem_Obi.nome}: {personagem_Obi.falar()}\n\n')
while personagem_Darth.get_hp() > 0:
  print(f"{ personagem_Darth.nome } (HP { personagem_Darth.get_hp() }) ataca { personagem_Obi.nome } (HP { personagem_Obi.get_hp() })")
  personagem_Darth.ataque(personagem_Obi)
  personagem_Obi.falar()
  print('-----------------------------')
  if personagem_Obi.get_hp() > 0:
    print(f"{ personagem_Obi.nome } (HP { personagem_Obi.get_hp() }) contra-ataca { personagem_Darth.nome } (HP { personagem_Darth.get_hp() })")
    personagem_Obi.contra_ataca(personagem_Darth)
    personagem_Darth.falar()
    print('-----------------------------')
  else:
    break