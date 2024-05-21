#29. Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cda
#km acima do limite.

velocidade = int(input('Qual a velocidade do carro: '))
if velocidade > 80:
    passou_velocidade = velocidade - 80
    multa = passou_velocidade * 7.0
    print(f"Você foi multado! O valor da multa é de R${multa:.2f}")
else:
    print("Dentro do limite de velocidade!")
