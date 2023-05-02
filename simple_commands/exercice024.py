"""
024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""

city = input("Please enter the city name: ")
city = city.strip()
if_starts_with_santo = city[:5].upper() == "SANTO"

if if_starts_with_santo:
    print("The name of the city starts with the word 'SANTO'.")
else:
    print("The name of the city don't starts with the word 'SANTO'.S")

"""
Correção:

cid = str(input("Digite o nome da cidade: "))
print(cid[:5].upper() == 'SANTO')

"""