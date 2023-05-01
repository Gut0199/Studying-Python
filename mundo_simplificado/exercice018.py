"""
018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse ângulo.
"""

from math import sin, cos, tan, radians

angle_cranes = float(input("Enter an angle in degrees: "))
angle_radians = radians(angle_cranes)
breast = sin(angle_radians)
cosine = cos(angle_radians)
tangent = tan(angle_radians)

print("The sine of the angle {} degrees is {:.2f}".format(angle_cranes, breast))
print("The cosine of the angle {} degrees is {:.2f}".format(angle_cranes, cosine))
print("The tangent of the angle {} degrees is {:.2f}".format(angle_cranes, tangent))

"""
Correção: 
from math import sin, cos, tan, radians 
angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))
"""
