"""
Faça um script que leia o ano de nascimento de sete pessoas. No final deve mostrar quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

current_year = date.today().year
legal_age = 0
minor = 0

for i in range(1, 8):
    year_of_birth = int(input(f"Enter the person's year of birth {i}: "))
    age = current_year - year_of_birth

    if age >= 18:
        legal_age += 1
    else:
        minor += 1

print("Adults: {}".format(legal_age))
print("Minors: {}".format(minor))


"""
Correção:

"""