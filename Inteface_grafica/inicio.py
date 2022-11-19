''' Teste Da Interface Grafica '''
import PySimpleGUI as sg

'''layout = [
        [sg.Text('Incluir Novo Cliente')],
        [sg.Text('Nome', size=(15,1)), sg.InputText('nome', key='primeiro_campo')],
        [sg.Submit(), sg.Cancel()],
        [sg.InputText('nome', key='segundo_campo')]
    ]

window = sg.Window('cadastro de clientes').Layout(layout)
button, values = window.Read()
print(button)
print(values)'''


class ExemploView:
    def __init__(self):
        self.__window = None
        self.init_components()


# usar os valores nas keys
# usar componente table para listar os dados
# listagem e opções em uma tela