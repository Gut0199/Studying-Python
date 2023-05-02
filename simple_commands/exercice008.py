"""
008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

meters = float(input("Please enter how much meters do you need to convert: "))
centimeters = meters * 100
millimeters = meters * 1000
print("Your conversion will have the result of {} Centimeters and {} Millimeters".format(centimeters, millimeters))

""""
Correção: 

medida = float(input("Uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
print("A medida de {}cm corresponde a {:.0f}cm e {:.0f}mm".format(medida, cm, mm))

"""