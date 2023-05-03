"""
036: Escreva um script em python que aprove o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

house_value = float(input("Enter home value: USD$ "))
salary = float(input("Enter the buyer's salary: USD$ "))
years = int(input("In how many years do you intend to pay? "))

installment = house_value / (years * 12)
limit = salary * 0.3

if installment <= limit:
    print("Loan approved")
    print("The value of the prepayment will be ${:.2f}".format(installment))
else:
    print("Loan Denied!")
    print("The value exceeds the 30% required.")
    print("Installment value: ${:.2f}".format(installment))
    print("Maximum installment limit: ${:.2f}".format(limit))

"""
Correção:

"""