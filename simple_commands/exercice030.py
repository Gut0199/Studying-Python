"""
030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("the number {} is even".format(number))
else:
    print("The number {} is odd".format(number))

"""
Correção:

numero = int(input("Me diga o um número qualquer: "))
resultado = numero % 2
if resultado == 0:
    print("O número {} é PAR".format(numero))
else:
    print("O número {} é IMPAR".format(numero))
    
"""