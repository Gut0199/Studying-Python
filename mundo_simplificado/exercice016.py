"""
016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""

real_number = float(input("Please enter a real number: "))
whole_portion = int(real_number)
print("The entire portion of {} is {}".format(real_number, whole_portion))

"""
Correção: 
from math import trunc
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))
"""