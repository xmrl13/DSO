from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia

class Imovel:
    def __init__(self, codigo: int, descricao: str, valor: float, locador: Locador):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = None
        self.__locatarios = []
        self.__mobilia = [Mobilia(codigo, descricao)]


    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def locador(self):
        return self.__locador

    @locador.setter
    def locador(self, locador):
        self.__locador = locador

    def incluir_locatario(self, locatario: Locatario):
        pass

    def excluir_locatario(self, codigo_locatario: int):
        pass

    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
        pass

    def excluir_mobilia(self, codigo_mobilia: int):
        pass

    def find_locatario_by_codigo(self, codigo_locatario: int):
        pass
