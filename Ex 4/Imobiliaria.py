from Imovel import Imovel


class Imobiliaria:
    def __init__(self):
        self.__imoveis = []

    @property
    def imoveis(self):
        return self.__imoveis

    def incluir_imovel(self, imovel: Imovel):
        if isinstance(imovel, Imovel):
            self.__imoveis.append(Imovel)

    def excluir_imovel(self, imovel: Imovel):
       self.__imoveis.pop(Imovel)