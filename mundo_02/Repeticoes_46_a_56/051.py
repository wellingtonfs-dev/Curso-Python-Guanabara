#51. Desenvolva um programa que leia o primeiro termo e a razão e uma PA. No final, mostre
#os 10 primeiros termos dessa progressão.

print('-=' *15)
print('      10 Primeiros PA')
print('-=' *15)


termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(termo, 10*razao + 1, razao):
    print(c, end='->')
print('FIM')
