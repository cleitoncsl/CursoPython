contador = 1
acumulador = 1

while contador <=10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1

else:
    print("Cheguei no Else")
print("isso será executado")