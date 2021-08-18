#
# Split, Join, Enumerate em python
# * Split - Dividir uma string # str
# * Join  - Juntar uma lista # str
# * Enumerate - Enumerar elementos da lista # list / iteráveis

string = 'O brasil é o Pais do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)

for palavra in lista1:
    print(f'a palavra {palavra}, \n apareceu {lista1.count(palavra)}x na frase.')