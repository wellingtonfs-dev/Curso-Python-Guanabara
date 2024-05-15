#19. Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
#programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice
lista = []
for n in range(1, 5):
    nome = input(f'Digite o {n}º nome: ')
    lista.append(nome)
escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}")