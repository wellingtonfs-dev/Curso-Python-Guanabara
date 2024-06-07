#78- Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
import sys

menor = sys.maxsize
maior = 0
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if valores[c] < menor:
        menor = valores[c]
    if valores[c] > maior:
        maior = valores[c]
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi {maior} na posições', end=' ')
for chave, valor in enumerate(valores):
    if valor == maior:
        print(f'{chave}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posições', end=' ')
for chave, valor in enumerate(valores):
    if valor == menor:
        print(f'{chave}...', end='')
print()

