#43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e
#mostre seu status, onde: abaixo de 18,5 é ABAIXO DO PESO; entre 18.5 e 25 é PESO
#IDEAL; 25 até 30 é SOBREPESO; 30 até 40 é OBESIDADE; acima de 40 é OBESIDADE MÓRBIDA.

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")