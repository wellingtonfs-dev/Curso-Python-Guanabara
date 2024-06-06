#77. Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois
#disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ("amor", "verde", "azul", "rosa", "jamaica", "bahia", "controle")

for palavra in tupla:
    print(f"\nNa palavra {palavra.upper()} temos: ", end="")
    for letra in range(0, len(palavra)):
        if palavra[letra] in 'aeiou':
            print(palavra[letra], end=" ")

