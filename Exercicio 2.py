class Cliente:
    def __init__(self, nome: str, cpf: int):
        self.nome = nome
        self.cpf = cpf


cliente1 = Cliente(123, 'Marcelo')
print(cliente1.cpf)
