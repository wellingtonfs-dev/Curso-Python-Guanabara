#22. Crie um programa que leia o nome completo de uma pessoa e mostre:
#(a) O nome com todas as letras maiúsculas e minúsculas.
#(b) Quantas letras ao todo (sem considerar espaços).
#(c) Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: '))
print(nome.upper())
print(nome.lower())
print(f"A quantidade de letras é {len(nome) - nome.count(" ")}")
separa = nome.split()
print(f"A quantidade de letras no primeiro nome é {len(separa[0])}")