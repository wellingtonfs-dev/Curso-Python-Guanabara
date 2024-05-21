#34. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
#aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os
#inferiores o iguais, o aumento é de 15%.

salario = float(input("Digite o salario: "))
if salario > 1250:
    salario_atual = salario + (salario * 10 / 100)
elif salario <= 1250:
    salario_atual = salario + (salario * 15 / 100)
print(f"O salário era R${salario:.2f} e com o aumento foi para R${salario_atual:.2f}")
