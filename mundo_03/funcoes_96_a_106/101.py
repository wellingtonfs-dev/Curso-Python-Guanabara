#Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date


def voto(ano_nasc):
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('VOTO NEGADO')
    elif 16 <= idade < 18 or idade > 65:
        print('VOTO OPCIONAL')
    elif idade >= 18:
        print('VOTO OBRIGATORIO')


ano_nasc = int(input('Digite o ano de nascimento: '))
voto(ano_nasc)
