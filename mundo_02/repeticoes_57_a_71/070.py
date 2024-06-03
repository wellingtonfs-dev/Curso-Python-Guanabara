#70. Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
#perguntar se o usuário vai continuar. No final, mostre:
#(a) Qual é o total gasto na compra.
#(b) Quantos produtos custam mais de R$1000.
#(c) Qual é o nome do produto mais barato.
import sys

soma_valor = 0
valor_maior_1000 = 0
mais_barato = sys.maxsize
produto_mais_barato = ''
while True:
    produto = input('Qual o nome do produto? ')
    valor = float(input('Qual o valor do produto? '))
    soma_valor += valor
    if valor < mais_barato:
        mais_barato = valor
        produto_mais_barato = produto
    if valor > 1000:
        valor_maior_1000 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
print(f"O total da compra foi de R${soma_valor:.2f}")
print(f"{valor_maior_1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato é o {produto_mais_barato} que custa R${mais_barato:.2f}")

