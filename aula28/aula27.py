secreto = 'Perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce Perdeu.')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('não vale digite apenas uma letra.')
        continue
    digitadas.append(letra)
    print(digitadas)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta!')
    else:
        print(f'letra {letra} não existe, na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Parabéns voce descobriu a palavra! {secreto} ')
        break
    else:
        print(f'A palavra secreta está assim: \n{secreto_temporario}')

    if not letra in secreto:
        chances -= 1
        print(f'Restam {chances}.')

