#Aprimore o desafio anterior, mostrando no final:
#a) A soma de todos os valores pares digitados.
#b) A soma dos valores da terceira coluna.
#c) O maior valor da segunda linha

linha = list()
matriz = list()
terceira_coluna = maior = pares = 0
for c in range(0, 3):
    for d in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{c}, {d}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('-='*30)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end='')
        if c == 1:
            if matriz[c][d] > maior:
                maior = matriz[c][d]
        if matriz[c][d] % 2 == 0:
            pares += matriz[c][d]
        if d == 2:
            terceira_coluna += matriz[c][d]
    print()
print('-='*30)
print(f"A soma de todos os valores pares digitados é {pares}.")
print(f"A soma dos valores da terceira coluna é {terceira_coluna}.")
print(f"O maior valor da segunda linha é {maior}.")

