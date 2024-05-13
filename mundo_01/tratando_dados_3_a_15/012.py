#12. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de
#desconto.

preco = float(input('Digite o preço do produto: R$ '))
preco_com_desconto = preco - (preco * 0.05)
print(f'O produto custa R${preco:.2f} e com o desconto de 5% vai custar R${preco_com_desconto:.2f}')
