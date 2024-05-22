#40. Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
#mensagem no final, de acordo com a média atingida: média abaixo de 5,0 é REPROVADO;
#média entre 5,0 e 6,9 fica de RECUPERAÇÃO; média 7,0 ou superior é APROVADO.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f"A média foi {media:.1f}")
if media < 5:
    print("O aluno está REPROVADO")
elif 5 <= media <= 6.9:
    print("O aluno está RECUPERAÇÃO")
elif media >= 7:
    print("O aluno está APROVADO")
