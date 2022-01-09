def ola_mundo():
    return 'Olá Mundo'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo())
print(executando)
