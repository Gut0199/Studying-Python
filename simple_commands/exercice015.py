"""
015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

km_traveled = float(input("Report the amount of kilometers traveled: Km"))
rented_days = int(input("Inform how many days it was rented: "))

price_day = 60.00
price_Km = 0.15

rent_cost = (rented_days * price_day) + (km_traveled * price_Km)

print("The total payable for renting a car will be R${:.2f}".format(rent_cost))


"""
Correção:

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
pago = (dias * 60) + (km * 0.15)
print("O total a pagar será de R${:.2f}".format(pago))

"""