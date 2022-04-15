l1 = '01234567890123456789012345678901234567890123456789'

lista = [letra for letra in l1]
n = 10
#comp = [(i, i + n) for i in range(0, len(l1), n)]
#comp = [i for i in range(0, len(l1), n)]
comp = [l1[i:i + n] for i in range(0, len(l1), n)]


print(comp)