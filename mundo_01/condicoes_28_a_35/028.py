#28. Escreva um programa que faça o computador "pensar"em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O
#programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

numero = randint(0, 5)
print("Pensei em um número de 0 a 5. Tente adivinhar...")
resposta = int(input("Qual número pensei? "))
if numero == resposta:
    print("Parabéns! Você venceu!")
else:
    print(f"Que pena! Você perdeu! Eu pensei no número {numero}")
