#26. Faça um programa que leia uma frase pelo teclado e mostre:
#(a) Quantas vezes aparece a letra "A".
#(b) Em que posição ela aparece pela primeira vez.
#(c) Em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase:')).strip().upper()
print(f"A letra 'A' aparece {frase.count('A')} vezes na frase.")
print(f"A letra 'A' aparece a primeira vez na posição {frase.find('A')}")
print(f"A letra 'A' aparece a ultima vez na posição {frase.rfind('A')}")