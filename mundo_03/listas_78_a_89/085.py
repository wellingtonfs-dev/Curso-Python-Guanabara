#Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

num = [[], []]
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º número: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print("Os números pares são", num[0])
print("Os números ímpares são", num[1])

