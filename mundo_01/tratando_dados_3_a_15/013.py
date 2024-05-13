#13. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com
#15% de aumento.

salario = float(input("Digite o salário do funcionario: R$ "))
aumento = salario + (salario * 0.15)
print(f"O salário do funcionario era R${salario:.2f} e com aumento de 15% fica R${aumento:.2f}")