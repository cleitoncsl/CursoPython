numero = input("Digite qual a Tabuada: ")
operador = input("Informe qual o operador que deseja utilzar:")
x = int(numero)
op = operador
while x <= x:
    y = 1
    print(f'Tabuada: {x}')
    print('#Inicio')
    while y <= 10:
        if op == '+':
            resultado = x + y
            print(f'{x} {op} {y} =', resultado)
            y += 1
        elif op == '-':
            resultado = x - y
            print(f'{x} {op} {y} =', resultado)
            y += 1
        elif op == '*':
            resultado = x * y
            print(f'{x} {op} {y} =', resultado)
            y += 1
        elif op == '/':
            resultado = x / y
            print(f'{x} {op} {y} =', f'{resultado:.4f}')
            y += 1
        else:
            print("hm..você digitou um operador que não existe..")
            break

    x += 1
    break
print("#FIM")
