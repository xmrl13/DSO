from logging import raiseExceptions
from Imovel import Imovel


class Imobiliaria:
    def __init__(self):
        self.__imoveis = []

    @property
    def imoveis(self):
        return self.__imoveis

    def incluir_imovel(self, imovel: Imovel):
        if (isinstance(imovel, Imovel)):
            for valor in self.__imoveis:
                if valor.codigo == imovel.codigo:
                    raiseExceptions('Imovel já cadastrado')
            self.__imoveis.append(imovel)

    def excluir_imovel(self, imovel: Imovel):
        if (isinstance(imovel, Imovel)):
            self.__imoveis.pop(imovel)