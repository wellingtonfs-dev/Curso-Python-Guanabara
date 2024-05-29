#63. Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
#primeiros elementos de uma Sequência de Fibonacci.

atual = 1
anterior = 0
seguinte = 0
numero = int(input("Digite um número: "))
print('Sequência de Fibonacci')
while numero > 0:
    print(anterior, end='')
    print(',' if numero > 1 else ' - ', end='')
    seguinte = atual + anterior
    anterior = atual
    atual = seguinte
    numero -= 1
print("FIM")




