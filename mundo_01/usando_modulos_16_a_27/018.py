#18. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
#e tangente desse ângulo.
import math

angulo = int(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Seno= {:.2f}'.format(seno))
print('Cosseno= {:.2f}'.format(cosseno))
print('Tangente= {:.2f}'.format(tangente))