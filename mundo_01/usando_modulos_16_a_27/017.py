#17. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
#triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")
