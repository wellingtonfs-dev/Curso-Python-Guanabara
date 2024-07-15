def aumentar(preco, taxa):
    preco = preco + (preco * taxa/100)
    return preco


def diminuir(preco, taxa):
    preco = preco - (preco * taxa/100)
    return preco


def dobro(preco):
    preco = preco * 2
    return preco


def metade(preco):
    preco = preco / 2
    return preco

