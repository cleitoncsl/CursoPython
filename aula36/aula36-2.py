cpf = input("Digite um CPF: ")
novo_cpf = cpf[:-2]
print(f'CPF digitado: {cpf}')
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso
    print(f' Digito: {index} -> {(novo_cpf[index])} * {reverso} = {total}')

    reverso -= 1
    if reverso < 2:
        reverso = 11
        print(f'reverso mudou para: {reverso}')
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

if(cpf == novo_cpf):
    print('CPF válido')
else:
    print('CPF inválido')