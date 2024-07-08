#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final coloque esse dicionário em
# ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep

jogadores = dict()
jogadores['jogador_1'] = randint(1, 6)
jogadores['jogador_2'] = randint(1, 6)
jogadores['jogador_3'] = randint(1, 6)
jogadores['jogador_4'] = randint(1, 6)

print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"O {k} tirou {v}")
    sleep(1)
print("  Ranking dos jogadores:")
jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
for i, v in enumerate(jogadores_ordenados):
    print(f"  {i +1}º lugar: {v[0]} com {v[1]}")
    sleep(1)



