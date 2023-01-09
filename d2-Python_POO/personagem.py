from personagem_interface import PersonagemInterface

# Para iniciar uma classe é necessário utilizar o método construtor __init__
class Personagem(PersonagemInterface):
    def __init__(self, nome, raca, hp):
      # Onde self.nome é a propriedade e nome é o atributo
      self.nome = nome
      self.raca = raca
      # Se eu colocar self._hp apenas estou informando que é protegido, mas continua sendo acessível
      # self.__hp torna a propriedade privada e apenas acessível por gets e sets
      self.__hp = hp

    # Podemos acessar pelo método get
    def get_hp(self):
      return self.__hp
    # Método set
    def set_hp(self, dano):
      self.__hp -= dano

    def falar(self):
      pass

   
    # Podemos acessar via property
    @property
    def hp(self):
      return self.__hp
    @hp.setter
    def hp(self, dano):
      self.__hp -= dano

