from personagem import Personagem
from sabre import Sabre
from random import choice

# A classe Personagem está vindo por herança
class Jedi(Personagem):
  def __init__(self, nome, raca, hp):
    super().__init__(nome, raca, hp)
    # A classe Sabre está vindo por composição
    self.sabre = Sabre('verde', 300)

  def defesa(self):
    defesa = choice([True, False])
    return defesa
  
  def contra_ataca(self, personagem):
    if not personagem.defesa():
      personagem.set_hp(self.sabre.poder)

  def falar(self):
    if self.get_hp() <= 0:
      print('Eu morri!! Lá se foi um Jedi')
    return 'Faça ou não faça, mas não tente!'
 
class Sith(Personagem):
  def __init__(self, nome, raca, hp):
    super().__init__(nome, raca, hp)
    self.sabre = Sabre('vermelho', 300)
    
  def ataque(self, personagem):
    # if personagem.defesa() is False - outra forma
    if not personagem.defesa():
      personagem.set_hp(self.sabre.poder)

  def defesa(self):
    defesa = choice([True, False])
    return defesa
  
  def falar(self):
    if self.get_hp() <= 0:
      print('Eu morri!! Lá se foi um Sith')
    return 'A força vem para quem a tem!'
  
  #  def __str__(self) -> str:
  #     return f""
  #               Name: {self.nome}
  #               Specie: {self.raca}
  #               HP: { self.get_hp()}
  #               LightSaber: { self.sabre} 
  #             "" 