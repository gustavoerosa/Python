nome = "Gustavo"
idade = 30
profissao = "Programador"
linguagem = "Python"
saldo = 10567146.16651

dados = {"nome": "Gustavo", "idade":30}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}" .format(nome, idade))

print("Nome: {0} Idade: {1}" .format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))

print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {age}" .format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")