# Modifique as funções que form criadas no desafio 107 para que elas aceitem um
# parâmetro a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"Aumentado 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))} ")
