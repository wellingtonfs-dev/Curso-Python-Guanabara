#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
#a) Quantas pessoas foram cadastradas
#b) A média de idade do grupo.
#c) Uma lista com todas as mulheres.
#d) Uma lista com todas as pessoas com idade acima da média.

galera = list()
pessoa = dict()
soma_idade = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'FM':
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'N':
        break
print('-=' * 30)
media = soma_idade / len(galera)
print(f"Foram cadastradas {len(galera)} pessoas.")
print(f"A média de idade do grupo foi {media:5.2f} anos")
print("As mulheres cadastradas foram: ")
for p in galera:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']} ", end='')
    print()
print("Listas das pessoas que estão acima da média:", end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')


