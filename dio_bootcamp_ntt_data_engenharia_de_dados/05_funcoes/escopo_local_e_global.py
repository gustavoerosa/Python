salario = 2000

def salario_bonus(bonus, lista):
    #lista.append(2)
    lista_auxiliar = lista.copy()
    lista_auxiliar.append(2)
    print(f"Lista auxiliar = {lista_auxiliar}")

    global salario
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)