"""
017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da Hipotenusa.
"""

from math import hypot

opposite_leg = float(input("Enter the length of the opposite leg: "))
adjacent_leg = float(input("Enter length of adjacent leg: "))
hypotenuse = hypot(opposite_leg, adjacent_leg)

print("The length of the hypotenuse is {:.2f}".format(hypotenuse))

"""
Correção: 

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h1 = (co * 2 + ca **2 ) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(h1)

OR 

from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h1 = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(h1))
"""