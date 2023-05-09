"""
044: Escreva um script que calcule o valor a ser pago por um produto, considerando o seu preço normal a condição de pagamento:
á vista dinheiro / cheque: 10% de desconto; á vista no cartão de crédito: 5% de desconto; em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros.
"""

price = float(input("Enter the product price: $ "))

print("Payment methods:")
print("1 - Cash / check.")
print("2 - Cash on credit card.")
print("3 - Up to 2 installments on your credit card.")
print("4 - In 3 or more installments on your credit card.")

option = int(input("What is your payment method? (1 to 4)"))

if option == 1:
    final_value = price - (price * 0.1)
    print("\n Cash / Check: Total to pay $ {:.2f}".format(final_value))
elif option == 2:
    final_value = price - (price * 0.05)
    print("\nCash on credit card: Total to pay $ {:.2f}".format(final_value))
elif option == 3:
    final_value = price
    print("\nUp to 2x on the card: Total to pay $ {:.2f}".format(final_value))
elif option == 4:
    installments = int(input("How many installments? "))
    final_value = price + (price * 0.2)
    installments_value = final_value / installments
    print("\n{}x in the card: Total to pay $ {:.2f}".format(installments, final_value))
    print("Value of each plot: ${:.2f}".format(installments_value))
else:
    print("\nInvalid option!!!")

"""
Correção:

preco = float(input('Preço da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista (cartão)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${parcela: .2f}
elif opcao == 4:    
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas Parcelas: '))
    parcela = total / totalparc 
    print('Sua compra será parcelada em {totalparc}x de R${parcela: .2f}
else:
    total = 0
    print('Opção inválida')
print(f'Sua compra de R${preco: .2f} vai custar R${total: .2f} no final.')

"""