class Eletrodomestico:
    def __init__(self, nome, cor, potencia, tensao, preco):
        self.nome = nome
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


class Secador(Eletrodomestico):
    pass


class Batedeira(Eletrodomestico):
    pass


class MaquinaDeLavar(Eletrodomestico):
    pass


secador = Secador('secador', "rosa", 55, 55, 35)
batedeira = Batedeira('batedeira', 'Azul', 66, 66, 89)
maqLavar = MaquinaDeLavar('máquina de lavar', 'Branca', 110, 110, 1550)

list_eletro = [secador, batedeira, maqLavar]
for eletro in list_eletro:
    print(f"O eletrodoméstico {eletro.nome} custa R$ {eletro.preco},00 reais")
