"""
042: Refaça o DESAFIO 35 dos triângulos, porém acrescente o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO todos os lados iguais, ISÓCELES dois lados iguais e um diferente, ESCALENO todos os lados diferentes.
"""

print("=="*20)
print("Analyzing Triangles!")
print("=="*20)

a = float(input("Enter the length of the first line:"))
b = float(input("Enter the length of the second line:"))
c = float(input("Enter the length of the third line:"))

if a < b + c and b < a + c and c < a + b:
    print("With these lengths it is possible to form a triangle!")
    if a == b == c:
        print("This triangle is an EQUILATERAL.")
    elif a == b or a == c or b == c:
        print("This is an ISOCELES triangle.")
    else:
        print("This is a SCALENE triangle.")
else:
    print("With these lengths it is not possible to form a triangle!")

"""
Correção:

"""