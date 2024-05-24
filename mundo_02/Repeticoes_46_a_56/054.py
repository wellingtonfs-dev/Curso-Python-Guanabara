#54. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
#pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime

menor = 0
maior = 0
for c in range(1, 8):
    ano_atual = datetime.today().year
    ano = int(input(f"Digite o {c}º ano de nascimento: "))
    idade = ano_atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(f"Ao todo tivemos {menor} menores de idade, e também tivemos {maior} maiores de idade")

