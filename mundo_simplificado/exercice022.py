"""
022: Crie um programa que leia o nome completo de uma pessoa e mostre:
1º O nome com todas as letras maiúsculas e minúsculas.
2º Quantas letras ao todo (sem considerar os espaços).
3º Quantas letras tem o primeiro nome.
"""

full_name = input("Please enter your full name: ")
print("Name in all capital letters {}".format(full_name.upper()))
print("Name in all lower case {}".format(full_name.lower()))
bunch_of_letters = len(full_name.replace(" ", ""))
print("Total number of letters {}".format(bunch_of_letters))
first_name = full_name.split()[0]
num_letters_first_name = len(first_name)
print("Number of letters in the first name {}".format(num_letters_first_name))

"""
Correção:

nome = str(input"Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
"""