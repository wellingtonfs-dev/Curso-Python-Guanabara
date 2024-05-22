#36. Escreva um programa para aprovar o empréstimo bancário para a compra de um casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A
#prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor da casa: '))
salario = float(input("Digite o salário do comprador: "))
ano =int(input('Quantos anos de financiamento? '))
valor_parcela = valor / (ano *12)
print(f"Para pagar uma casa de R${valor:.2f} em {ano} anos o valor da parcela será de R${valor_parcela:.2f}")
if(valor_parcela <= salario * 0.30):
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")
