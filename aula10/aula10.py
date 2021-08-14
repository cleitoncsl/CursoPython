nome = input("Qual o seu nome: ")
idade = input("Qual sua idade: ")

if idade.isdigit() and not nome.isdigit():
    idade = int(idade)
    qtde_carac_nome = len(nome)
    # Limite Empréstimo
    idade_menor = 20  # muito jovem
    idade_maior = 30  # passou da idade

    if qtde_carac_nome <= 4:
        print('Digite um nome valido!')
    else:
        if idade_menor <= idade <= idade_maior:
            print(f'{nome} voce pode pegar o empréstimo')
        else:
            print(f'{nome}, voce não pode pegar o empréstimo.')
else:
    print("Digite valores corretos")
