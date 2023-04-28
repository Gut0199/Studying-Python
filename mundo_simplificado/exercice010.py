"""
010: Crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

dolar = 5.50
valor_real = float(input("Please, enter how much do you have: "))
valor_dolar = valor_real / dolar
print("With R$ {:.2f}, you can to by $ {:.2f}".format(valor_real, valor_dolar))


"""
Correção:
real = float(input("Quanto de dinheiro você tem na carteira? R$"))
dolar = real / 5.50
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))

"""