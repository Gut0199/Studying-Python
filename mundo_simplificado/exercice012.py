"""
012: Faça um programa que leia o preço de uma produto e mostre seu novo preço. com 5% de desconto.
"""

price = float(input("Please enter the price of the product: $"))

discount = price * 0.05
new_price = price - discount

print("With 5% discount, the new product price will be {}".format(new_price))


"""
Correção:
preco = float(input("Qual é o preço do produto? R$"))
novo = preco - (preco * 5 / 100)
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(preco, novo))

"""