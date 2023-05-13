"""
Refaça o desafio 009, porém dessa vez utilizando a estrutura for.
"""

number = int(input("Please enter an integer: "))

print(f"Number table {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


"""
Correção:

"""