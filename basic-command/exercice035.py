"""
035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

side1 = float(input("Enter the measurement of the first side: "))
side2 = float(input("Enter the measurement of the second side"))
side3 = float(input("Enter the measurement of the third side"))

if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2):
    print("The measurements entered form a triangle.")
else:
    print("The measurements entered don't form a triangle")

"""
Correção:
print("-="*20)
print("Analisador de Triângulos")
print("-="*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
    print("Os segmentos podem formar um triângulo!")
else:
    print("Os segmentos não podem formar um triângulo!")

"""