"""
008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

meters = float(input("Please enter how much meters do you need to convert: "))
centimeters = meters * 100
millimeters = meters * 1000
print("Your conversion will have the result of {} Centimeters and {} Millimeters".format(centimeters, millimeters))