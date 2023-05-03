"""
033: Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# bigger number:
if num1 >= num2 and num1 >= num3:
    bigger = num1
elif num2 >= num1 and num2 >= num3:
    bigger = num1
else:
    bigger = num3

# smaller number:
if num1 <= num2 and num1 <= num3:
    smaller = num1
elif num2 <= num1 and num2 <= num3:
    smaller = num2
else:
    smaller = num3

print("The biggest number is {}".format(bigger))
print("The smallest number is {}".format(smaller))

"""
Correção:

a = int(input("Primeiro valor: "))
d = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}".format(menor)
print("O maior valor digitado foi {}".format(maior))
"""
