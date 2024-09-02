contatos = {"gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}}

resultado = contatos.pop("gustavo@gmail.com")
print(resultado)

resultado = contatos.pop("gustavo@gmail.com", {})
print(resultado)