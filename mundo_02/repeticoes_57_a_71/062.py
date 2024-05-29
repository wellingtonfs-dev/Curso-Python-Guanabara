#62. Melhore o exercício 061, perguntando para o usuário se ele quer mostrar mais alguns
#termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('-=' *15)
print('      10 Primeiros PA')
print('-=' *15)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
count = 0
resposta = 1
total = 10
while resposta != 0:
    total = total + resposta
    while count <= total:
        print(termo, end='->')
        termo += razao
        count += 1
    print("Pausa")
    resposta = int(input("\nDigite quantos termos a mais você deseja ver: "))
print('FIM')
