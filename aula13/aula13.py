""""""""
# :s - strings
# :d - inteiro
# :f - Números flutuantes
# :.(Numero)f - Quantidade de casas decimais
# :(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)

# > - Esquerda
# < - Direita
# ^ - Centro

""""""""

numero1 = 10
numero2 = 3
divisao = numero1 / numero2
print('{:.4f}'.format(divisao))
print(f'{divisao:.2f}')
print(f'{numero2:0>10}')
print(f'{numero2:0>3}')
print(f'{numero2:0<3}')
print(f'{numero2:0>10.2f}')
print(f'{numero2:0<10.2f}')
nome = 'Otavio'
sobrenome = 'Miranda'
print((50-len(nome)) / 2)
print(f'{nome:#^50}')
nome_formatado = '{:@>19}'.format(nome)
nome_formatado1 = '{:@<19}'.format(nome)
nome_formatado2 = '{:@^20}'.format(nome)
sobre_nome = '{1:#^10}'.format(nome,sobrenome)
sobre_nome2 = '{0:#^10}' '{1:@^50}'.format(nome,sobrenome)
print(nome_formatado)
print(nome_formatado1)
print(nome_formatado2)
print(sobre_nome)
print(sobre_nome2)

nome = 'otavio miranda'
print(nome.title())