#44. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
#preço normal e condição de pagamento: à vista dinheiro/cheque: 10% DE DESCONTO;
#à vista no cartão: 5 DE DESCONTO; em até 2x no cartão: PREÇO NORMAL; 3x ou
#mais no cartão: 20% DE JUROS.

valor = int(input('Digite um valor da compra: '))
menu = f"""
==================FORMA DE PAGAMENTO==================
1 - à vista em dinheiro/cheque
2 - à vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão"""
print(menu)

opcao = int(input('Opção de pagamento: '))
if opcao == 1:
    total = valor - valor * 0.1
elif opcao == 2:
    total = valor - valor * 0.05
elif opcao == 3:
    total = valor
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f}')
elif opcao == 4:
    total = valor + valor * 0.2
    qtd_parcelas = int(input('Quantas parcelas? '))
    parcela = total / qtd_parcelas
    print(f'Sua compra será parcelada em {qtd_parcelas}x de R${parcela:.2f} COM JUROS')
else:
    total = valor
    print("Opção inválida de pagamento, tente novamente!")
print(f"Sua compra de R${valor:.2f} vai custar R${total:.2f} no final")

