#74. Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois
#disso, mostre a listagem de números gerados e também indique o menor e o maior valor
#que estão na tupla.
import sys
from random import randint

menor = sys.maxsize
maior = 0
tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os valores sorteados foram: ', end='')
for c in tupla:
    print(f"{c}", end=" ")
print(f"\nO maior número sorteado foi {max(tupla)}")
print(f"O menor número sorteado foi {min(tupla)}")

