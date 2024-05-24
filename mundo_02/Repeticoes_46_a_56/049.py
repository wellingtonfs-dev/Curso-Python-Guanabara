#49. Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só
#que agora utilizando um laço FOR.

numero = int(input('Digite um número: '))
print(f"Tabuada do {numero}")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")