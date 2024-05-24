#53. Crie um programa que leia uma frase qualquer e diga se ela é um políndromo,
# desconsiderando os espaços. Exemplo: apos a sopa é um políndromo.


frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print(f"A frase {frase} é um políndromo")
else:
    print(f"A frase {frase} NÃO é um políndromo")



