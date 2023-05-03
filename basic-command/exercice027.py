"""
027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""

full_name = input("Please enter your full name: ")
separate_name = full_name.split()
first_name = separate_name[0]
last_name = separate_name[-1]
print("Your first name is: {}".format(first_name))
print("Your last name is: {}".format(last_name))

"""
Correção:

n = str(input("Digite o seu nome completo: )).strip()
nome = n.split()
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é {}".format(nome[len(nome)-1]))

"""