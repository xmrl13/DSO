from Imovel import Imovel


class Imobiliaria:
    def __init__(self):
        self.__imoveis = []

    @property
    def imoveis(self):
        return self.__imoveis

    def incluir_imovel(self, imovel: Imovel):
        if (imovel is not None) and (isinstance(imovel, Imovel)
                                     and (imovel not in self.__imoveis)):
            if imovel not in self.__imoveis:
                self.__imoveis.append(imovel)

    def excluir_imovel(self, imovel: Imovel):
        for chave, valor in enumerate(self.__imoveis):
            if valor == imovel:
                self.__imoveis.pop(chave)
