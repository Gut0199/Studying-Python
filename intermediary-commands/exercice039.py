"""
039: Faça um script em python que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu script também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
current_year = date.today().year

year_of_birth = int(input("Enter the year of birth: "))
age = current_year - year_of_birth

if age < 18:
    print("still {} years left for enlistment.".format(18 - age))
    print("Enlistment will be {}".format(current_year + (18 - age)))
elif age == 18:
    print("It's time to enlist!")
else:
    print("It's been {} years past the enlistment deadline.".format(age - 18))
    print("Enlistment should have been done in {}".format(current_year - (age - 18)))

"""
Correção:


from datetime import date
atual = date.today().year
nasc = int))input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade 
    ano = atual + saldo
    print('Ainda faltam {saldo} anos para o alistamento.')
    print('Seu alistamento será em {}')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {saldo} anos.')
    print('Seu alistamento foi em {}')

"""