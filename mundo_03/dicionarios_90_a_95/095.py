#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes do aproveitamento de cada jogador

jogador = dict()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    for c in range(0, jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols na {c+1}ª partida? ')))
        jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        resp = input("Deseja continuar? [S/N] ").upper()[0]
        if resp in 'SN':
            break
        print("Erro! Resposta tem que ser S ou N.")
    if resp == 'N':
        break
print("-=" * 40)
print(f'{"Cod":<4}{"Nome":<15}{"Partidas":<15}{"Gols":<15}{"Total":<15}')
print("__"*40)
for i, v in enumerate(time):
    print(f"{i:<4}", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("__"*40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! Não existe o jogador com o código {busca}")
    else:
        print(f"Levantamento do jogador {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"  No jogo {i + 1} fez {g} gols")
        print("__" * 40)
