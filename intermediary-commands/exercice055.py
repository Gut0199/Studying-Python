"""
Faça um script em Python que leia o peso de cinco pessoas e que no final mostre qual foi o maior e o menor peso lido.
"""

weights = []

for i in range(1, 6):
    weight = float(input("Enter the person's weight {}: ".format(i)))
    weights.append(weight)

greater_weight = max(weights)
lower_weight = min(weights)

print("The highest weight read was: {}kg".format(greater_weight))
print("The lowest weight read was: {}kg".format(lower_weight))

"""
Correção:

"""