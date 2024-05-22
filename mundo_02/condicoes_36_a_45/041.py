#41. A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos é MIRIM; até 14
#anos é INFANTIL, até 19 anos é JUNIOR, até 25 anos é SÊNIOR; acima é MASTER.
from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nascimento
print(f"O atleta tem {idade} anos, ", end='')
if idade <= 9:
    print("Categoria MIRIM")
elif idade <= 14:
    print("Categoria INFANTIL")
elif idade <= 19:
    print("Categoria JUNIOR")
elif idade <= 25:
    print("Categoria SÊNIOR")
else:
    print("Categoria MASTER")
