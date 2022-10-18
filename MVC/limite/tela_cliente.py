

class TelaCliente:

    def mostra_tela_opcoes(self):
        print('*' * 20)
        print('Clientes')
        print('*' * 20)
        print('1 - Incluir Cliente')
        print('2 - Excluir Cliente')
        print('3 - Listar Clientes')
        print('4 - Alterar Clientes')
        print('0 - Voltar')
        opcao = int(input('Digite uma opção: '))
        return opcao

    def pega_dados_cliente(self):
        print('CADASTRO DO CLIENTE')
        nome_cliente = input('Nome do CLiente: ')
        fone_cliente = input('Fone do CLiente: ')
        return {'nome_cliente': nome_cliente,
                'fone_cliente': fone_cliente}

    def mostra_cliente(self, dados_cliente):
        print('CLIENTE')
        print(f"Nome: {dados_cliente['nome_cliente']}")
        print(f"Nome: {dados_cliente['fone_cliente']}")
