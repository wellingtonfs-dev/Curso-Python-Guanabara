#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente
# de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).capitalize()
ano = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
pessoa['idade'] = ano_atual - ano
pessoa['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))
if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    ano_contribuicao = 35 - (ano_atual - pessoa['contratação'])
    pessoa['aposentadoria'] = pessoa['idade'] + ano_contribuicao
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
