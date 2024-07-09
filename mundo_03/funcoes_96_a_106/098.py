#Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que
# realizar três contagens através da função criada:
#a) De 1 até 10, de 1 em 1
#b) De 10 até 0, de 2 em 2
#c) Uma contagem personalizada.
from time import sleep


def contador(ini, fim, passo):
    print("-=" * 20)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f"Contagem de {ini} até {fim} de {passo} em {passo} ")
    if ini < fim:
        for c in range(ini, fim + 1, passo):
            print(c, end=' ')
            sleep(0.3)
        print('FIM')
    elif ini > fim:
        for c in range(ini, fim - 1, -passo):
            print(c, end=' ')
            sleep(0.3)
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(ini, fim, passo)
