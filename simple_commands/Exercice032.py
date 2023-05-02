"""
032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("{} it's a leap year".format(year))
else:
    print("{} is not a leap year".format(year))

"""
Correção:

from datetime import date 
ano = int(input("Que ano quer analisar? "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} não é BISSEXTO".format(ano))


"""