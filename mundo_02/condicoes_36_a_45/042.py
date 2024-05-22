#42. Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
#triângulo será formado: todos os lados iguais é EQUILÁTERO; dois lados iguais é ISÓSCELES;
# todos os lados diferentes é ESCALENO.

reta1 = int(input('Digite um valor: '))
reta2 = int(input('Digite outro valor: '))
reta3 = int(input('Digite mais um valor: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        print("Essas medidas formam um triângulo EQUILÁTERO")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("Essas medidas formam um triângulo ISÓSCELES")
    else:
        print("Essas medidas formam um triângulo ESCALENO")
else:
    print("NÃO FORMAM UM TRIÂNGULO")