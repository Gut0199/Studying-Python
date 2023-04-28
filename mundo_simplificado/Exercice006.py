"""
006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a sua raiz quadrada.
"""

import math

number = int(input("Please enter a some number: "))
double = number * 2
triple = number * 3
square_root = math.sqrt(number)
print("The number {}, has as its double {}, and its triple as {} and its square root is {:.2f}".format(number, double, triple, square_root))

"""
Correção:
"""