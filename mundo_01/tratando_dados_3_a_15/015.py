#15. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
#o carro custa R$60 por dia e R$0,15 por km rodado.

quant_km = float(input('Quantos Km: '))
dias = int(input('Quantos dias: '))
valor = (quant_km * 0.15) + (dias * 60)
print(f'O valor do aluguel do carro com {quant_km} km rodados e o {dias} dias de aluguel foi de R${valor:.2f}')