#68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
#quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
#no final do jogo.

from random import randint
print("-=" * 20)
print(" " * 7 + "Vamos jogar par ou ímpar")
print("-=" * 20)
vitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input("Digite um valor: "))
    escolha = ' '
    while escolha not in 'PI':
        escolha = input("Par ou Ímpar? [P/I] ").strip().upper()[0]
    soma = computador + jogador
    print(f"Você jogou {jogador} e o computador {computador}. Total deu {soma},", end=" ")
    if escolha == "P":
        if soma % 2 == 0:
            print("DEU PAR - Jogador ganhou!")
            vitorias += 1
        else:
            print("DEU ÍMPAR - Computador ganhou!")
            break
    elif escolha == "I":
        if soma % 2 == 0:
            print("DEU PAR - Computador ganhou!")
            break
        else:
            print("DEU ÍMPAR - Jogador ganhou!")
            vitorias += 1
print(f"GAME OVER - você venceu {vitorias} vez(es)!")
