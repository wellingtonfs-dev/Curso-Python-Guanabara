#37. Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
#qual será a base de conversão: 1 pra binário; 2 para octal; 3 para hexadecimal.

numero = int(input("Digite um numero: "))
print("""
=========MENU=========
    1 - Binário
    2 - Octal
    3 - Hexadecimal
======================
""")
opcao = int(input("Digite uma opção do menu: "))
if opcao == 1:
    numero_binario = bin(numero)
    print(f"O número {numero} em binário é {numero_binario[2:]}")
if opcao == 2:
    numero_octal = oct(numero)
    print(f"O número {numero} em octal é {numero_octal[2:]}")
if opcao == 3:
    numero_hex = hex(numero)
    print(f"O número {numero} em hexadecimal é {numero_hex[2:]}")
else:
    print("Opção inválida. Tente novamente!")
