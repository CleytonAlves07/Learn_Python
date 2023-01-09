from personagem import Personagem

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

