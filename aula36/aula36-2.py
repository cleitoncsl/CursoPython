cpf = '16899535009'
novo_cpf = cpf[:-2]
#print(novo_cpf)
#print(f'--{novo_cpf}--')
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11