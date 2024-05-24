#52. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número: "))
cont = 0
for c in range(1, numero+1):
    if numero % c == 0:
        cont += 1
if cont == 2:
    print(f'O número {numero} é PRIMO')
else:
    print(f'O número {numero} NÃO É PRIMO')
