#Crie um programa que gerencie o aproveitamento de uma jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em dicionário, incluindo o total de gols
# feitos durante o campeonato.

jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
for c in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    jogador['total'] = sum(jogador['gols'])
print("-=" * 20)
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
for k, v in enumerate(jogador['gols']):
    print(f'  => Na {k + 1}ª partida fez {v} gols')
print(f"Foi um total de {jogador['total']} gols")



