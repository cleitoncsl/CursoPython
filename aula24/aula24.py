l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)
l1.extend(l2)
print(l1)
l1.extend('b')
print(l1)
l2.append('2')
print(l2)
l2.insert(0, 'banana') # eu escolho onde quero ele
print(l2)
l2.pop()
print(l2)
