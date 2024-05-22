#45. Crie um programa que faça o computador jogar JOKENPÔ com você.
from random import randint

menu = f"""
============MENU============
    0 - Pedra
    1 - Papel
    2 - Tesoura
    9 - Sair
============================"""
print(menu)
while True:
    jokenpo = ["Pedra", "Papel", "Tesoura"]
    computador = randint(0, 2)
    jogador = int(input("Faça sua jogada: "))
    if jogador == 9:
        break
    print("Resultado:")
    if computador == 0:
        if jogador == 0:
            print("EMPATE")
        elif jogador == 1:
            print("JOGADOR VENCEU")
        elif jogador == 2:
            print("COMPUTADOR VENCEU")
        else:
            print("Jogada inválida")
    elif computador == 1:
        if jogador == 0:
            print("COMPUTADOR VENCEU")
        elif jogador == 1:
            print("EMPATE")
        elif jogador == 2:
            print("JOGADOR VENCEU")
        else:
            print("Jogada inválida")
    elif computador == 2:
        if jogador == 0:
            print("JOGADOR VENCEU")
        elif jogador == 1:
            print("COMPUTADOR VENCEU")
        elif jogador == 2:
            print("EMPATE")
        else:
            print("Jogada inválida")
    print(menu)
