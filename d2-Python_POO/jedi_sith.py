from personagem import Personagem
from sabre import Sabre

# A classe Personagem está vindo por herança
class Jedi(Personagem):
  def __init__(self, nome, raca, hp):
    super().__init__(nome, raca, hp)
    # A classe Sabre está vindo por composição
    self.sabre = Sabre('verde', 200)


     
class Sith(Personagem):
  def __init__(self, nome, raca, hp):
    super().__init__(nome, raca, hp)
    self.sabre = Sabre('vermelho', 300
    
  def ataque(self, personagem):
    personagem.set_hp(self.sabre.poder)
