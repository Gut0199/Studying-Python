"""
041: A confederação nacional de natação precisa de um script que leia o ano de nascimento de um atleta e mostre a sua categoria de acordo com a idade: Até 9 anos MIRIM, até 14 anos INFANTIL, até 19 anos JÚNIOR, até 25 anos SÊNIOR, acima de 25 anos MASTER.
"""
from datetime import date

year_of_birth = int(input("Enter the athlete's year of birth: "))

age = date.today().year - year_of_birth

if age <= 9:
    category = "Little"
elif age <= 14:
    category = "Children's"
elif age <= 19:
    category = "Junior"
elif age <= 25:
    category = "Senior"
else:
    category = "Master"

"""
Correção:

"""