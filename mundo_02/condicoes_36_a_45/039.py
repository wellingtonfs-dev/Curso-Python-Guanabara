#39. Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
#sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se
#já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que
#falta ou que passou do prazo.
from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos.")
if idade == 18:
    print("Você tem que se alistar imediatamente")
elif idade < 18:
    print(f"Falta {18 - idade} ano(s) para você se alistar")
elif idade > 18:
    print(f"Está {idade - 18} ano(s) atrasado para o alistamento")
