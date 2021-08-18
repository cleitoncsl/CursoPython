# for / else

variavel = ['Luiz Otávio', 'joãozinho', 'MAria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('a'):
        comeca_com_j = True
        print(comeca_com_j)
        break
else:
    print('nao existe')
