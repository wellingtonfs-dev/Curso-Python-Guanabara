def aumentar(preco=0, taxa=0):
    preco = preco + (preco * taxa/100)
    return preco


def diminuir(preco=0, taxa=0):
    preco = preco - (preco * taxa/100)
    return preco


def dobro(preco=0):
    preco = preco * 2
    return preco


def metade(preco=0):
    preco = preco / 2
    return preco


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
