class Cabeça:
    def __init__(self, expressao):
        self.expressao = expressao

    def __str__(self):
        return f'Cabeça ({self.expressao})'


class Boneco:
    def __init__(self, nome, expressao_cabeca):
        self.nome = nome
        self.cabeca = Cabeça(expressao_cabeca)

    def destruir(self):
        print(f"{self.nome} foi destruído!")
        del self.cabeca  

    def __str__(self):
        return f'Boneco {self.nome} com {self.cabeca}'

boneco1 = Boneco("Bob", "Feliz")
print(boneco1)

boneco2 = Boneco("Alice", "Surpresa")
print(boneco2)

boneco1.destruir()