#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final, mostre um boletim contendo a média de cada
# um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

turma = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    turma.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print("-="*40)
print(f"{'No.':<4}{'Nome':<10}{'Média':>8}")
print("_"*26)
for c in range(0, len(turma)):
    print(f"{c:<4}{turma[c][0]:<10}{turma[c][2]:>8.1f}")
print('-='*40)
while True:
    notas = int(input('Mostrar nota de qual aluno?(999 interrompe): '))
    if notas == 999:
        print('FINALIZANDO...')
        print('-='*40)
        break
    if notas >= len(turma):
        print('Notas acima do intervalo. Tente novamente.')
    else:
        print(f"Notas de {turma[notas][0]} são {turma[notas][1]}")



