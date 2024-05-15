#23. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
#separados.

texto = input('Digite um número de 0 à 9999: ')
if len(texto) > 4:
    print("Não pode ter mais de 4 caracteres")
else:
    print("COM STRING")
    texto_completo = texto.zfill(4)
    print(f"""
Milhar: {texto_completo[0]}
Centena: {texto_completo[1]}
Dezena: {texto_completo[2]}
Unidade: {texto_completo[3]}
""")

    print("COM INT")
    numero = int(texto)

    unidade = numero % 10
    dezena = numero // 10 % 10
    centena = numero // 100 % 10
    milhar = numero // 1000
    print(f"""
Milhar: {milhar}
Centena: {centena}
Dezena: {dezena}
Unidade: {unidade}
""")





