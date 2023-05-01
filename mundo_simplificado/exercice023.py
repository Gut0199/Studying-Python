"""
023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

number = int(input("Enter a number from 0 to 9999: "))
thousand = number // 1000
hundred = (number // 100) % 10
ten = (number // 10) % 10
unit = number % 10

print("Thousand: {}".format(thousand))
print("Hundred: {}".format(hundred))
print("Ten: {}".format(ten))
print("Unit: {}".format(unit))

"""
Correção:
num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisando o número {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

"""