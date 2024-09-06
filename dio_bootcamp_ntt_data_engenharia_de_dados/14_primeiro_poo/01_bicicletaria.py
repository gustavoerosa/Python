class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmm...")

    #def __str__(self):
    #    return f"Bicicleta: Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.title()}: {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

print()
print("=" * 30)
print()

b2 = Bicicleta("Verde", "Monark", 2000, 189)
b2.buzinar #Bicicleta.buzinar(b2)
print(b2)
b2.correr()