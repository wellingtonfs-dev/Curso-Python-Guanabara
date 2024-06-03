#67. Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
#valor digitado pelo usuário. O programa será interrompido quando o número solicitado
#for negativo.

while True:
    numero = int(input("Qual tabuada deseja ver(número negativo para parar): "))
    print("-=" * 30)
    if numero < 0:
        break
    else:
        print(f"TABUADA DO {numero}")
        for c in range(1, 11):
            print(f"{numero} x {c} = {numero * c}")
    print("-=" * 30)
print("PROGRAMA TABUADA ENCERRADO")