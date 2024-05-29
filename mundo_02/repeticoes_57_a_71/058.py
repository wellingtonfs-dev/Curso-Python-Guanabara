#58. Melhore o jogo do exercício 028 onde o computador vai "pensar"em um número entre 0 e
#10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
#palpites foram necessários para vencer.
from random import randint

computador = randint(0, 10)
palpite = 0
acertou = False
while not acertou:
    pessoa = int(input("Digite seu palpite de 0 a 10: "))
    palpite += 1
    if pessoa == computador:
        acertou = True
    else:
        if pessoa < computador:
            print("Mais...")
        elif pessoa > computador:
            print("Menos...")
print(f"Você ganhou! Com {palpite} tentativas!")


