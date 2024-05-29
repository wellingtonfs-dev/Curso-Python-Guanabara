#65. Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O
#programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
import sys

menor = sys.maxsize
soma = maior = contador = 0
resposta = 'S'
while resposta != 'N':
    numeros = int(input("Digite um número: "))
    contador += 1
    soma += numeros
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / contador
print(f"A média de todos os números é {media:.2f} o maior valor foi {maior} e o menor valor foi {menor}")

