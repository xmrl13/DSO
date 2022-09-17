"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):

        self.array_para_ordenar = array_para_ordenar

    def ordena(self):

        array_do_ordena = self.array_para_ordenar
        array_ordenado = []

        for numero in array_do_ordena:
            for chave, valor in enumerate(array_ordenado):
                if numero < valor:
                    array_ordenado.insert(chave, numero)
                    break
            else:
                array_ordenado.append(numero)
        array_para_ordenar = array_ordenado
        return array_para_ordenar

    def toString(self):

        nova_string = ''
        string_ordenado = self.ordena()
        string_ordenado = str(string_ordenado).strip('[]')
        string_ordenado = str(string_ordenado).strip(' ')
        for i in range(len(string_ordenado)):
            if string_ordenado[i] != ' ':
                nova_string = nova_string+string_ordenado[i]
        print(nova_string)
        print(type(nova_string))
        return nova_string

ordenar = Ordenacao([9,4,2,8,4,13,54,87,1])
ordenar.ordena()
ordenar.toString()
