#Crie um programa que tenha uma função fatorial() que receba dois parametros:
#o primeiro que indique o número a calcular e o outro chamado show, que será
#um valor lógico(opcional) indicando se será mostrado ou não na tela o processo
#de cálculo do fatorial.

def fatorial(num, show=False):
    """
    => Calcula o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número num
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} ', end='= ')
    return f

print(fatorial(5, True))
help(fatorial)



