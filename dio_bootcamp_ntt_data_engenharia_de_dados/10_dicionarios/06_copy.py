contatos = {"gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["gustavo@gmail.com"] = {"nome": "Gu"}

print(contatos["gustavo@gmail.com"])

print(copia["gustavo@gmail.com"])