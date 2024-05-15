#16. Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
#porção inteira. Exemplo: o número 6,127 tem a parte inteira 6.

from math import trunc

numero = float(input('Digite um número: '))
numero_inteiro = trunc(numero)
print(f"O valor digitado é {numero} e sua parte inteira é {numero_inteiro}")