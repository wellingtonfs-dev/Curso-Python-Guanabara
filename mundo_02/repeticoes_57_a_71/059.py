#59. Crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar a
#operação solicitada em cada caso: [1] somar; [2] multiplicar; [3] maior; [4] novos números;
#[5] sair do programa.

numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))

menu = """
=====================MENU=====================
[1] - SOMAR
[2] - MULTIPLICAR
[3] - DIVISAR
[4] - NOVOS NÚMEROS
[5] - SAIR
==============================================
"""
print(menu)
opcao = 0
while opcao != 5:
    opcao = int(input('Digite sua opcao: '))
    if opcao == 1:
        soma = numero1 + numero2
        print(f"A soma de {numero1} + {numero2} = {soma}")
    if opcao == 2:
        multiplicacao = numero1 * numero2
        print(f"A multiplicação de {numero1} * {numero2} = {multiplicacao}")
    if opcao == 3:
        divisao = numero1 / numero2
        print(f"A divisão de {numero1} / {numero2} = {divisao}")
    if opcao == 4:
        numero1 = float(input('Digite um numero: '))
        numero2 = float(input('Digite outro numero: '))




