#
# Split, Join, Enumerate em python
# * Split - Dividir uma string # str
# * Join  - Juntar uma lista # str
# * Enumerate - Enumerar elementos da lista # list / iteráveis

string = 'O Brasil é o Pais do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
# print(lista2)
palavra = ''
contagem = 1
palavras_rep = []
for valor in lista1:
    qtd_vezes = lista1.count(valor)
    if qtd_vezes >= 2:
        print(f' qtde: {qtd_vezes} - letra: {valor}')

    if qtd_vezes >= 2:
        contagem = qtd_vezes
        palavra = valor
        palavras_rep.append(valor)
        lista_final = list(dict.fromkeys(palavras_rep))


print(lista_final)
print(f'A(s) palavra(s) que mais se repetiram foram: {lista_final} - {contagem}. Elas repetiram no minimo 2x.')