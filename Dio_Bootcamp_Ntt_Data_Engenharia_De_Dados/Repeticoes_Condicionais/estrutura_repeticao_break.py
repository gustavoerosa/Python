while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
        #continue

    if numero % 2 == 0:
        continue

    print(numero)


for numero in range(100):

    if numero % 2 == 0:
        #break
        continue

    print(numero, end=" ")