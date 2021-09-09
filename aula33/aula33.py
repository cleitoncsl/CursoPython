lista = [
    ['Edu', 'Joao', 'Luiz'],
    ['Vilson', 'Lucas', 'Ygor'],
    ['Helena', 'Ed', 'Lu']
]

enumerada = list(enumerate(lista))
#print(enumerada)

for v1 in enumerate(lista, 53):
    print(v1)