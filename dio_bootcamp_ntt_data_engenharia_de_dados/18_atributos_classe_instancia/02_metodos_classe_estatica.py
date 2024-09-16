class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    # Preciso ter contexto da classe? = Método de Classe
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    # Não preciso de contexto, classe e nem da instância do objeto? = Método Estático
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Gustavo", 30)
# print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1993, 12, 22, "Gustavo")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))