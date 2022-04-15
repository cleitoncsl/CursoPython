l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

tupla = (
    ('chave' , 'valor'),
    ('chave2' , 'valor2'),
)

ex5 = [(x, y) for x, y in tupla]
ex6 = dict(ex5)


l3 = list(range(100))
ex7 = [v for v in l3 if v % 2 == 0]
ex8 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
ex9 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]



print(ex9)