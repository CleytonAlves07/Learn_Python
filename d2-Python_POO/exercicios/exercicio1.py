class Ventilador:
    def __init__(self, cor, potencia, tensao, preco):
        self.cor = cor
        self.preco = preco
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_max = 3

    def ligar(self, velocidade):
        if 0 > velocidade > self.__velocidade_max:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.velocidade_max}")

        self.__velocidade = velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.ventilador = None

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def __str__(self):
        if (self.ventilador):
            return f"{self.nome} possui R$ {self.saldo_na_conta},00 reais na sua conta"
        return f"{self.nome} não comprou o ventilador"


ventilador1 = Ventilador("azul", 50, 5, 850)
cliente1 = Pessoa("Eli", 18500)
cliente1.comprar_ventilador(ventilador1)

print(cliente1)
