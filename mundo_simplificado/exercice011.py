"""
011: Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

width = float(input("please enter the width of the wall in meters: "))
height = float(input("please enter the height of the wall in meters: "))

area = width * height
liters_of_ink = area / 2

print("The area of the wall is {:.2f} m².".format(area))
print("You will need to {:.2f} liters of paint it.".format(liters_of_ink))

"""
Correção:
larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
print("Sua parede tem a dimensão de {}x{} e a sua Área é de {}m²".format(larg, alt, area))
tinta  = area / 2
print("Para pintar essa parede você precisará de {} litros de tinta".format(tinta))

"""