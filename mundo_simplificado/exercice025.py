"""
025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

name = input("Please enter the full name: ")
name = name.strip()
with_has_silva = 'SILVA' in name.upper().split()

if with_has_silva:
    print("The name {} has 'SILVA'.".format(name))
else:
    print("The name {} has't 'SILVA.'".format(name))

"""
Correção:

nome = str(input("Qua é o nome que deseja consultar?: "))
print("O nome contém Silva? {}".format('silva' in nome.lower()))

"""