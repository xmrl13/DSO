from abc import  ABC, abstractmethod
class Figura(ABC):

    @abstractmethod
    def __init__(self, pontos=[]):
        print('Instanciou construtor de figura')
        self.__pontos = pontos

    def desenhe (self):
        for ponto in self.__pontos:
            print(ponto)

#----------------------------------------------------------

class Circulo(Figura):

    def __init__(self, ponto_1, raio):
        print('CONSTRUTOR DE CIRCULO')
        super().__init__([ponto_1])
        self.__raio = raio

    def desenhe(self):
        super().desenhe() #Utilizando o super.()desenhe() o metodo da classe pai é invocado, no caso abstrata a classe é
        # abstrata mas com metodo concreto que pode ser utilizado.
        print('Desenho do Triangulo', self.__raio)

#---------------------------------------------------------------------------
class Quadrado(Figura):
    def __init__(self, ponto_1, ponto_2, ponto_3, ponto_4, lado):
        print('CONSTRUTOR QUADRADO')
        super().__init__([ponto_1, ponto_2, ponto_3, ponto_4])
        self.__lado = lado


    def desenhe(self):
        super().desenhe()
        print('Desenho do quadrado lados', self.__lado)

class Triangulo(Figura):
    def __init__(self, base, altura, h):
        print('Construtor do triangulo')
        super().__init__([base, altura])
        self.__base = base
        self.__altura = altura

    def desenhe(self):
        super().desenhe()
        print(f'Triangulo de base {self.__base}, altura {self.__altura}')


ciruclo = Circulo(1, 2)
quadrado = Quadrado(1,2,3,4,5)
triangulo = Triangulo(1, 2, 5)
figuras = []
figuras.append(ciruclo)
figuras.append(quadrado)
figuras.append(triangulo)
figuras.append('Oi eu não sou uma figura')

for figuras in figuras:
    figuras.desenhe()