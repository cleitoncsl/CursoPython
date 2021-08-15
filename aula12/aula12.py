nome = input("Qual o seu nome? ")
numero = input("Digite um número: ")
len_nome = len(nome)
if not nome.isdigit() and len_nome >=4:
    if not numero.isdigit():
        print("Você nao digitou um número. Seu animal..")
    else:
        numero = int(numero)
        if numero%2==0:
            from datetime import datetime
            data_atual = datetime.now()
            hora_completa = data_atual.strftime("%H:%M:%S")
            data_completa = data_atual.strftime("%d/%m/%Y")
            hora = data_atual.strftime("%H")
            print("-----------------------")
            print(f'| Data-->> {data_completa} |')
            print("-----------------------")
            print(f'| Hora-->> {hora_completa} |')
            print("-----------------------")
            print(f'| Hora-->> {hora} |')
            print("-----------------------")
            hora = int(hora)
            if hora >=1 and hora <12:
                print(f'Bom dia!{nome}')
            elif hora>=12 and hora <18:
                print(f'Boa tarde! {nome}')
            elif hora>=18 and hora ==0:
                print(f'Boa Noite{nome}')
            else:
                print("wtf algum erro")
            print("O numero é par")
        else:
            print(f'{nome}, o número {numero}, não é um numero par.')
else:
    print("Nome Inválido")