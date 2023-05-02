"""
031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,40 para viagens mais longas.
"""

distance = float(input("Enter the travel distance in km: "))
if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.4
print("The ticket price is R${:.2f}".format(price))

"""
Correção: 

distancia = float(input("Qual é a distância da sua viagem? "))
print("Você esta prestar a começar uma viadem de {}km".format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(preco))
 
"""