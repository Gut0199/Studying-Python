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

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima podem formar um triângulo ', end=='')
    if r1 == r2 == r3:
        print('EQUILÁERO.')
    elif r1 != r2 != r3 != r1
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmento acima não podem formar um triângulo!')
    
"""