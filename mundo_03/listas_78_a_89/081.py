#81 - Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#a)Quantos números foram digitados.
#b)A lista de valores ordenada de forma decrescente.
#c)Se o valor 5 foi digitado e está ou não na lista

numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print("="*40)
print(f"Você digitou {len(numeros)} valores.")
numeros.sort(reverse=True)
print(f"Os valores em ordem decrescente fica {numeros}")
if 5 in numeros:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")
