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
n = int(input("Digite um número: "))
d = n * 2
t = n * 3
r = n ** (1/2)
print("O dobro de {} vale {}".format(n, d))
print("O triplo de {} vale {}".format(n, t))
print("A raiz quadrada de {} é igual á {:.2f}".format(n, r))

OR 

n = int(input("Digite um número: "))
print("O dobro de {} vale {}".format(n, (n*2)))
print("O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}".format(n, (n*3), n, (n**(1/2)))

OR 

n = int(input("Digite um número: "))
print("O dobro de {} vale {}".format(n, (n*2)))
print("O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}".format(n, (n*3), n, pow(n, (1/2))))
"""