#7. Desenvolva um programa que leia as duas notas de um aluno e mostre a sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite o segunda nota: '))
media = (nota1 + nota2) / 2
print(f"O aluno com a primeira nota {nota1} e a segunda nota {nota2} ficou com média = {media:.2f}")
