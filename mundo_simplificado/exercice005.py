"""
005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

number = int(input("Please enter some number: "))
predecessor = number - 1
sucessor = number + 1
print(f"The predecessor of {number} is {predecessor} and the sucessor of {number} is {sucessor}")

"""
Correção:
n = int(input("Digite um número: "))
a = n - 1 
b = n + 1
print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(n, a, b))
or 
print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(n, (n-1), (n+1)))
"""