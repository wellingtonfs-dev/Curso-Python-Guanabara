#75. Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
#(a) Quantas vezes apareceu o valor 9.
#(b) Em que posição foi digitado o primeiro valor 3.
#(c) Quais foram os números pares.

lista = []
for c in range(1, 5):
    numero = int(input(f'Digite o {c}º valor: '))
    lista.append(numero)
tupla = tuple(lista)
print(tupla)
print('-='*40)
print(f"O valor 9 apareceu {tupla.count(9)} vez(es).")
print('-='*40)
if 3 in tupla:
    print(f"O primeiro 3 foi digitado na {tupla.index(3)+1}º posição.")
else:
    print(f"O número 3 não foi digitado em nenhuma posição")
print('-='*40)
print(f"Os números pares foram:", end=" ")
for c in tupla:
    if c % 2 == 0:
        print(c, end=" ")


