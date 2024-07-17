# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print("\033[0;31mErro! Digite um número inteiro valido.\033[m ")
            continue
        except KeyboardInterrupt:
            print("\033[0;31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except ValueError:
            print("\033[0;31mErro! Digite um número real valido.\033[m ")
            continue
        except KeyboardInterrupt:
            print("\033[0;31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return f


n = leiaInt("Digite um número inteiro: ")
f = leiaFloat("Digite umnúmero real: ")
print(f"Você acabou de digitar o número inteiro {n} e o real {f}")

