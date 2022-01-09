print()
print('Texto Explicativo.')

respostas_certas = 0
perguntas = {
    'Pergunta 1': {
        'pergunta' : 'Quanto é 2 + 2?',
        'respostas' : {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa' : 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 x 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '6'},
        'resposta_certa': 'c',
    },
}
print()
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print(f'Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EH , voce acertou!!!')
        respostas_certas += 1
    else:
        print('IXXI voce errou')

    print()

qtd_perguntas = len(perguntas)
porcentagem_perguntas = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} resposta(s)')
print(f' Sua porgentagem foi {porcentagem_perguntas}%.')