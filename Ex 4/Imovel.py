from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia


class Imovel:
    def __init__(self, codigo: int, descricao: str,
                 valor: float, locador: Locador):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = locador
        self.__locatarios = []
        self.__mobilias = []

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
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def locador(self):
        return self.__locador

    @locador.setter
    def locador(self, locador):
        pass

    @property
    def locatarios(self):
        return self.__locatarios

    @property
    def mobilias(self):
        return self.__mobilias

    def incluir_locatario(self, locatario: Locatario):
        if isinstance(locatario, Locatario):
            if locatario not in self.__locatarios:
                self.__locatarios.append(locatario)

    def excluir_locatario(self, codigo_locatario: int):
        for chave, valor in enumerate(self.__locatarios):
            if chave == codigo_locatario:
                self.__locatarios.pop(chave)

    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
        verifica = False
        for valor in self.__mobilias:
            if valor.codigo == codigo_mobilia:
                verifica = True
        if not verifica:
            self.__mobilias.append(Mobilia(codigo_mobilia, descricao_mobilia))

    def excluir_mobilia(self, codigo_mobilia: int):
        for chave, valor in enumerate(self.__mobilias):
            if chave == codigo_mobilia:
                self.__mobilias.pop(chave)

    def find_locatario_by_codigo(self, codigo_locatario: int):
        for chave, valor in enumerate(self.__locatarios):
            if valor.codigo == codigo_locatario:
                print(f'Locatario encontrado, codigo = {codigo_locatario}'
                      f', apontando para: {self.__locatarios[chave]}')
                return self.__locatarios[chave]
            else:
                print('Locatario não encontrado')


imovel1 = Imovel(45, 'Casa', 1500, Locador(1234, 'Marcelo', 456, 'ABC'))
imovel1.incluir_locatario(Locatario(13, 'Marcelo', 456))
imovel1.find_locatario_by_codigo(13)
