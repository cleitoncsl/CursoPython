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
nome = 'Otavio Miranda'
print((50-len(nome)) / 2)
print(f'{nome:#^50}')
