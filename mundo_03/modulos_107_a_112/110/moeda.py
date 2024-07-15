def aumentar(preco=0, taxa=0, format=False):
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)


def dobro(preco=0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco=0, format=False):
    res = preco / 2
    return res if format is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxa=10, reducao=5):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f"{'Preço analisado:':<20}{moeda(preco):<10}")
    print(f"{'Dobro do preço:':<20}{moeda(dobro(preco)):<10}")
    print(f"{'Metade do preço:':<20}{moeda(metade(preco)):<10}")
    print(f"{f'{taxa}% de aumento:':<20}{moeda(aumentar(preco, taxa)):<10}")
    print(f"{f'{reducao}% de redução:':<20}{moeda(diminuir(preco, reducao)):<10}")
    print('-' * 40)
