# Adapte o código do desafio #107, criando uma função adicional
# chamada moeda() que consiga mostrar os números como um valor
# monetário formatado.

import moeda

preco = float(input("Digite o preço: R$"))
moeda.resumo(preco, 10, 12)
