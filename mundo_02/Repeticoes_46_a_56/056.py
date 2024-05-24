#56. Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#(a) A média de idade do grupo.
#(b) Qual é o nome do homem mais velho.
#(c) Quantas mulheres têm menos de 20 anos.


soma_idade = 0
nome_mais_velho = ""
idade_mais_velho = 0
mulheres = 0

for c in range(1, 5):
    print(f"========== {c}º Pessoa ==========")
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: ").strip())
    soma_idade += idade
    sexo = input("Digite o sexo(m/f): ").strip()
    if idade > idade_mais_velho and sexo in 'Mm':
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo in "Ff" and idade < 20:
        mulheres += 1
print(f'A média de idade do grupo é {soma_idade/4}')
print(f'O nome do homem mais velho é {nome_mais_velho} e a idade dele é {idade_mais_velho} anos')
print(f'Tem {mulheres} mulheres com menos de 20 anos')