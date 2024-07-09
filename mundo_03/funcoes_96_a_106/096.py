#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular(largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    a=largura*comprimento
    return f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de {a:.1f}m²."


print("  Controle de Terrenos")
print("-"*25)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
print(area(largura, comprimento))
