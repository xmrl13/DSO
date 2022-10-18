import sys

from View.tela_principal import TelaPrincipal
from Controller.controlador_cliente import ControladorCliente

class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_cliente = ControladorCliente(self)

    def inicia_clientes(self):
        self.__controlador_cliente.mostra_tela_opcoes()

    def inicia_notas_fiscais(self):
        print('NOTAS FISCAIS')

    def finaliza(self):
        sys.exit()

    def inicia(self):
        opcoes = {1: self.inicia_clientes, 2: self.inicia_notas_fiscais, 0: self.finaliza}
        while True:
            opcao = self.__tela_principal.mostra_tela_inicial()
            opcoes[opcao]()
