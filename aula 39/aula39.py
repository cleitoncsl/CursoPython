clientes = {
    'cliente1' : {
        'nome' : 'luiz',
        'sobrenome' : 'Otavio'
    },
    'cliente2' : {
        'nome' : 'Joao',
        'sobrenome' : 'Moreira',
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Jose',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k} = {dados_v}')