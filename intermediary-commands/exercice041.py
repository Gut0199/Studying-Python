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

from datime import date 
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JUNIOR.')
elif idade <= 25:
    print('SÊNIOR.')
else:
    print('MASTER.')
"""