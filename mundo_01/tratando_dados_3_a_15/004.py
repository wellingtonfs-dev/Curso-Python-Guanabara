#4. Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
#as informações possíveis sobre ele.

tipo = input('Digite algo: ')
print(f"O tipo primitivo desse valor é {type(tipo)}")
print(f"É um número? {tipo.isnumeric()}")
print(f"É um alfabético? {tipo.isalpha()}")
print(f"É um alfanumérico? {tipo.isalnum()}")
print(f"Está em maiúsculas? {tipo.isupper()}")
print(f"Está em minúscula? {tipo.islower()}")
print(f"Está capitalizada? {tipo.istitle()}")
print(f"Só tem espaços? {tipo.isspace()}")



