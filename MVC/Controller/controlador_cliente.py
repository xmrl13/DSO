
from View.tela_cliente import TelaCliente
from Model.cliente import Cliente

class ControladorCliente:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_cliente = TelaCliente()
        self.__clientes = []

    def inclui_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados_cliente['nome_cliente'],
                          dados_cliente['fone_cliente'])
        if not self.retorna_cliente_pelo_nome(cliente.nome):
            self.__clientes.append(cliente)

    def retorna_cliente_pelo_nome(self, nome):
        for cliente in self.__clientes:
            if cliente.nome == nome:
                return cliente

    def altera_cliente(self):
        pass

    def exclui_cliente(self):
        pass

    def lista_cliente(self):
        for cliente in self.__clientes:
            dados_cliente = {'nome_cliente': cliente.nome,
                             'fone_cliente': cliente.fone}
            self.__tela_cliente.mostra_cliente(dados_cliente)

    def mostra_tela_opcoes(self):
        opcoes = {1: self.inclui_cliente,
                  2: self.exclui_cliente,
                  3: self.lista_cliente,
                  4: self.altera_cliente
                  }
        while True:
            opcao = self.__tela_cliente.mostra_tela_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
