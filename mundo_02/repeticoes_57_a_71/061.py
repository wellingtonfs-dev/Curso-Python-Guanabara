#61. Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10
#primeiros termos da progressão usando a estrutura WHILE.

print('-=' *15)
print('      10 Primeiros PA')
print('-=' *15)


termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
count = 0
while count < 10:
    print(termo, end='->')
    termo += razao
    count += 1
print('FIM')
