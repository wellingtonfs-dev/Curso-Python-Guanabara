# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada
# resumo(), que mostre na tela algumas informações geradas pelas funções que já
# temos no módulo criado até aqui.
import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}")
print(f"Aumentado 10%, temos {moeda.aumentar(preco, 10, True)} ")
