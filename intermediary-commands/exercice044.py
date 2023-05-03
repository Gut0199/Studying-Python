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

"""