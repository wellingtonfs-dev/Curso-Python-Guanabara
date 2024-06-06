#73. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
#Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#(a) Os 5 primeiros times.
#(b) Os últimos 4 colocados.
#(c) Times em ordem alfabética.
#(d) Em que posição está o time do Vasco.

tabela = ("Flamengo", "Bahia", "Botafogo", "São Paulo", "Athletico-PR", "Bragantino", "Palmeiras", "Internacional",
          "Cruzeiro", "Atlético-MG", "Fortaleza", "Juventude", "Grêmio", "Vasco", "Fluminense", "Criciúma",
          "Corinthians", "Atlético-GO", "Vitória", "Cuiabá")
print('-=' * 20)
print(f"Os 5 primeiros times são: {tabela[:5]}")
print('-=' * 20)
print(f"Os últimos 4 colocados são: {tabela[-4:]}")
print('-=' * 20)
print(f"Times em ordem alfabética: {sorted(tabela)}")
print('-=' * 20)
print(f"A posição do Vasco na tabela é {tabela.index("Vasco") + 1}º")
