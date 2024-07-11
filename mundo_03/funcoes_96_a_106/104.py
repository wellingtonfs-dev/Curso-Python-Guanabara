# Crie um mprograma que tenha a função leiaInt(), que vai funcionar de forma
# semelhante à função input() do python, só que fazendo a validação para aceitar
# apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')

def leiaInt(msg):
    while True:
        aux = str(input(msg))
        if aux.isnumeric():
            return int(aux)
        else:
            print("\033[0;31mErro! Digite um número inteiro valido.\033[m ")


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")