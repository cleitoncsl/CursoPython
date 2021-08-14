nome = "Luiz Otávio"

altura = 1.80
peso = 80
ano_nascimento = 1981
ano_atual = 2021
idade = ano_atual - ano_nascimento
e_maior = idade > 18
imc = peso / (altura ** 2)

print(f'{nome}, tem {idade}, anos de idade, e seu imc é {imc:.2f}, e tem {idade} anos.')