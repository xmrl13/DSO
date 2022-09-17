'''
class Pagina:
    def __init__(self, numero: int, texto: str):
        self.numero = numero
        self. texto = texto


class Livro:
    def __init__(self, titulo: str, numero_pagina: int, texto_pagina: str):
        self.titulo = titulo
        self.paginas = []
        pagina = Pagina(numero_pagina, texto_pagina)
        self.paginas.append(pagina)

    def add_pagina(self, numero_pagina: int, texto_pagina: str):
        pagina = Pagina(numero_pagina, texto_pagina)
        self.paginas.append(pagina)

#pagina = Pagina(1, 'Do nada para a escuridão')

livro1 = Livro('A cabana', 1, 'Do nada para a escuridão')

#livro2 = Livro()
print(livro1)

'''

# class Membro:
#     def __init__(self, nome:str ='', telefone: int = None):
#         self.nome = nome
#         self.telefone = telefone
#
#
# class Clube:
#     def __init__(self, nome: str = ''):
#         self.nome = nome
#         self.mebros = []

#    def add_membro(self, membro: Membro):

'''
class Animal:
    def __init__(self, nome, tamanho):
        print('Construtor do animal')
        self.nome = nome
        self.tamanho = tamanho


class Gato(Animal):
    def __init__(self, nome: str = '', tamanho: str = '', vidas: int = ...):
        print('Construtor do gato')
        self.vidas = vidas
        super().__init__(nome, tamanho)

    def miar(self):
        print('Miau')

gato1 = Gato('Magnelson', 'Pequeno', 15)
print(gato1.nome,
      gato1.tamanho,
      gato1.vidas)
'''