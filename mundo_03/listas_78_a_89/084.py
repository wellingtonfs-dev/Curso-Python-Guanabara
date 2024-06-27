#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
#No final mostre:
#a)Quantas pessoas foram cadastradas.
#b)Uma listagem com as pessoas mais pesadas
#c)Uma listagem com as pessoas mais leves
import sys

temp = list()
pessoas = list()
maior_peso = 0
menor_peso = sys.maxsize
maior_galera = list()
menor_galera = list()
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    pessoas.append(temp[:])
    temp.clear()
    for p in pessoas:
        if p[1] > maior_peso:
            maior_peso = p[1]
        if p[1] < menor_peso:
            menor_peso = p[1]
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f"Foram cadastradas {len(pessoas)} pessoas.")

for p in pessoas:
    if maior_peso == p[1]:
        maior_galera.append(p[0])
    if menor_peso == p[1]:
        menor_galera.append(p[0])
print(f"O maior peso foi de {maior_peso:.1f}Kg. Peso de {maior_galera}")
print(f"O menor peso foi de {menor_peso:.1f}Kg. Peso de {menor_galera}")