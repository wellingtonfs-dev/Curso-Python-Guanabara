#60. Faça um programa que leia um número qualquer e mostre o seu fatorial.

numero = int(input("Digite um número: "))
fatorial = 1
contador = numero
print(f"{numero}! = ", end="")
while contador > 0:
    print(contador, end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)



