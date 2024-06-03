#69. Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#(a) Quantas pessoas tem mais de 18 anos.
#(b) Quantos homens foram cadastrados.
#(c) Quantas mulheres tem menos de 20 anos.

maiores = 0
mulheres = 0
homens = 0
contador = 1

while True:
    print(f"========== {contador}º Pessoa ==========")
    idade = int(input("Digite a idade: ").strip())
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("Digite o sexo(m/f): ").strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input("Deseja continuar? [S/N]").strip().upper()[0]
    contador += 1
    if continuar == "N":
        break
print(f'Tem {maiores} pessoas com mais de 18 anos')
print(f'Tem {homens} homens cadastrados')
print(f'Tem {mulheres} mulheres com menos de 20 anos')