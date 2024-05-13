#10. Crie um programa que leia quanto dinheiro uma pessoas tem na carteira e mostre quantos
#dólares ela pode comprar. Considere U$$1,00 = R$3,37

valor = float(input('Digite a quantidade que tem na carteira: R$ '))
dolar = valor / 3.37
print(f"Com R${valor:.2f} você consegue comprar US${dolar:.2f}")