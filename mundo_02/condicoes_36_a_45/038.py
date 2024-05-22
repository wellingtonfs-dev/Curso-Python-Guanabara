#38. Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma
#mensagem: o primeiro valor é maior; o segundo valor é maior; não existe valor maior, os
#dois são iguais.

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}")
if numero2 > numero1:
    print(f"O número {numero2} é maior que o número {numero1}")
if numero1 == numero2:
    print("Os números são iguais")
