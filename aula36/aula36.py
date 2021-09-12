import random

Cpf = input("Digite o CPF: ")
novo_cpf = int(Cpf[:-2])
print(novo_cpf)
list = []

for i in novo_cpf:
    n = i
    if len(list) <= 9:
        list.append(i)
print(list)

soma = (list[0] * 10) + \
       (list[1] * 9) + \
       (list[2] * 8) + \
       (list[3] * 7) + \
       (list[4] * 6) + \
       (list[5] * 5) + \
       (list[6] * 4) + \
       (list[7] * 3) + \
       (list[8] * 2)

print(soma)
teste = (11 - (soma % 11))
print(f' Resultado é {teste}')
if teste > 9:
    d1 = 0
    print(f'{teste} é maior que 9. ')
else:
    d1 = teste
    print(f'{teste} é menor que 9. ')
list.append(d1)
print(list)

soma1 = (list[0] * 11) + \
        (list[1] * 10) + \
        (list[2] * 9) + \
        (list[3] * 8) + \
        (list[4] * 7) + \
        (list[5] * 6) + \
        (list[6] * 5) + \
        (list[7] * 4) + \
        (list[8] * 3) + \
        (list[9] * 2)

print(soma1)
teste1 = (11 - (soma1 % 11))
print(f' Resultado é {teste1}')
if teste1 >= 9:
    d2 = 0
    print(f'{teste1} é maior que 9. ')
else:
    d2 = teste1
    print(f'{teste1} é menor que 9. ')
list.append(d2)
print(list)