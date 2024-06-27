#Faça um program,a que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('='*40)
print(f"{'JOGA NA MEGA SENA':^40}")
print('='*40)
jogo = list()
qtd_jogos = int(input("Quantos jogos você que que eu sorteie? "))
print("-="*3, f"SORTEANDO {qtd_jogos} JOGOS", "-="*3)
for i in range(0, qtd_jogos):
    for j in range(0, 6):
        while True:
            num = int(randint(1, 60))
            if num not in jogo:
                jogo.append(num)
                break
            else:
                num = int(randint(1, 60))
    jogo.sort()
    print(f'Jogo {i+1}: {jogo}')
    sleep(1)
    jogo.clear()
print("-="*5, f"Boa sorte", "-="*5)
