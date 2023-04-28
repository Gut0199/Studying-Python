"""
009: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

number = int(input("Please enter some number tha you want: "))
zero = 0 * number
one = 1 * number
two = 2 * number
three = 3 * number
four = 4 * number
five = 5 * number
six = 6 * number
seven = 7 * number
eight = 8 * number
nine = 9 * number
ten = 10 * number

print("The table of this number will be: "
      f"\n0 x {number} = {zero}"
      f"\n1 x {number} = {one}"
      f"\n2 x {number} = {two}"
      f"\n3 x {number} = {three}"
      f"\n4 x {number} = {four}"
      f"\n5 x {number} = {five}"
      f"\n6 x {number} = {six}"
      f"\n7 x {number} = {seven}"
      f"\n8 x {number} = {eight}"
      f"\n9 x {number} = {nine}"
      f"\n10 x {number} = {ten}")


"""
Correção: 
print("-"*20)
num = int(input("Digite um número para ver a sua tabuada: "))
print("{} x {} = {}".format(num, 1, num*0))
print("{} x {} = {}".format(num, 1, num*1))
print("{} x {} = {}".format(num, 2, num*2))
print("{} x {} = {}".format(num, 3, num*3))
print("{} x {} = {}".format(num, 4, num*4))
print("{} x {} = {}".format(num, 5, num*5))
print("{} x {} = {}".format(num, 6, num*6))
print("{} x {} = {}".format(num, 7, num*7))
print("{} x {} = {}".format(num, 8, num*8))
print("{} x {} = {}".format(num, 9, num*9))
print("{} x {} = {}".format(num, 10, num*10))
print("-"*20)

"""