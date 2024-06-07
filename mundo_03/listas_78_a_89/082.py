#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares
#e os valores ímpares digitados, respectivamente.
#No final, mostre o conteúdo das três listas geradas

valores = list()
impares = list()
pares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])
print("=" * 40)
print(f'Os valores digitados foram {valores}')
print(f'Os pares digitados foram {pares}')
print(f'Os ímpares digitados foram {impares}')