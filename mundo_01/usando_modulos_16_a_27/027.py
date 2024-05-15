#27. Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
#primeiro e o último nome separadamente. Exemplo: Ana Maria de Souza, primeiro: Ana,
#último: Souza.

nome = str(input('Digite seu nome: '))
nome_separado = nome.split()
print(f"Primeiro nome: {nome_separado[0]}")
print(f"Último nome: {nome_separado[-1]}")