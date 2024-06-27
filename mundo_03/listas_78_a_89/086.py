#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
# lidos pelo teclado.No final mostre a matriz na tela, com a formatação correta.

linha = list()
matriz = list()
for c in range(0, 3):
    for d in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{c}, {d}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('-='*30)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()



