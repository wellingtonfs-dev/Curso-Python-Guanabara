#Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES
# sorteados pela função anterior.
from random import randint


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end='')
    for c in range(0, 5):
        num = randint(1, 10)
        print(num, end=' ')
        lista.append(num)
    print('PRONTO')


def somaPar(listas):
    print(f'Somando os valores pares de {listas}, temos ', end='')
    soma = 0
    for num in listas:
        if num % 2 == 0:
            soma += num
    print(soma)


numeros = list()
sorteia(numeros)
somaPar(numeros)
