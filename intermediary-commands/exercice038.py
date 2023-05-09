"""
038: Escreva um script em python que leia dois números inteiros e compare-os mostrando na tela uma mensagem: O primeiro valor é maior; O segundo valor é maior; Não existe valor maior, ambos são equivalentes.
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("The first value is greater!")
elif num2 > num1:
    print("The second value is greater!")
else:
    print("The values ??are the same!")

"""
Correção:

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Os dois valores são iguais')
    
"""