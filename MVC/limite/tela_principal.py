class TelaPrincipal:
    def mostra_tela_inicial(self):
        print('*' * 20)
        print('Sistema Vendas')
        print('*' * 20)
        print('1 - Clientes')
        print('2 - Notas Fiscais')
        print('0 - Sair')
        opcao = int(input('Esccolha a opção: '))
        return opcao