#55. Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e
#o menor peso lidos.
import sys

maior = 0
menor = sys.maxsize

for c in range(1, 6):
    peso = float(input(f'Digite o {c}º peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'Maior peso foi: {maior}Kg')
print(f'Menor peso foi: {menor}Kg')