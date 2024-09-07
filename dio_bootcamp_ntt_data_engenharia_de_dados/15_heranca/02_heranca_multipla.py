class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.title()}: {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

    # def __str__(self):
    #     return "Mamifero"

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

    # def __str__(self):
    #     return "Ave"

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, numero_patas, cor_pelo, cor_bico):
        super().__init__(numero_patas = numero_patas, cor_pelo = cor_pelo, cor_bico = cor_bico)

        #print(Ornitorrinco.__mro__)
        print(Ornitorrinco.mro()) 

    # def __str__(self):
    #     return "Ornitorrinco"

gato = Gato(numero_patas = 4, cor_pelo = "Preto")
print(gato)

print()
print("=" * 30)
print()

ornitorrinco = Ornitorrinco(numero_patas = 2, cor_pelo = "Vermelho", cor_bico = "Laranja")
print(ornitorrinco)