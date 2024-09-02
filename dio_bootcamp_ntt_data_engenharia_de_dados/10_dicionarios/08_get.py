contatos = {"gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {}) 
print(resultado)

resultado = contatos.get(
    "gustavo@gmail.com", {}
)
print(resultado)