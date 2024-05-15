#20. O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos
#dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem
#sorteada.

from random import shuffle
lista = []
for n in range(1, 5):
    nome = input(f'Digite o {n}º nome: ')
    lista.append(nome)
shuffle(lista)
print(f"A ordem de apresentação será:")
print(lista)
