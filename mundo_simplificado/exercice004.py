"""
004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possíveis sobre ele.
"""

phrase = input("Please enter a sentence: ")
print("About Phrase: ")
print("1º Valor is", phrase)
print("2º Type is", type(phrase))
print("3º Is alphanumeric?", phrase.isalnum())
print("4º Is alphabetic?", phrase.isalpha())
print("5º Is numeric?", phrase.isnumeric())
print("6º Is decimal?", phrase.isdecimal())
print("7º Is it composed of only spaces?", phrase.isspace())
print("8º is it uppercase?", phrase.isupper())
print("9º is it lowercase?", phrase.islower())

"""
Correção:
a = input("Digite algo: ")
print("O tipo primitivo desse valor é", type(a))
print("Só tem espaços?", a.isspace())]
print("É um número?", a.isnumeric())
print("É alfabético?".isalpha())
print("É alfanumérico?", a.isalnum())
print("Está em maiúsculas?", a.isupper())
print("Está em minúsculas?", a.islower())
print("Está capitalizado?, a.istitle())

"""