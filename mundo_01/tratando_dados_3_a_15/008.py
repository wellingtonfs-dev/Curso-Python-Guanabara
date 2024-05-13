#8. Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
#e milímetros.

medida = float(input('Digite um valor em metros: '))
centimetros = medida * 100
milimetros = medida * 1000
print(f"A medida de {medida} metros é igual a {centimetros:.0f} em centímetros e {milimetros:.0f} em milímetros.")