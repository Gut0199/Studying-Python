"""
Faça um script em python que leia o nome, a idade e o sexo de 4 pessoas e que no final mostre:
A média de idade do grupo; Quem é o mais velho e qual o seu nome; Quantas mulheres fazem parte do grupo.
"""

ages = []
names = []
womans = 0

for i in range(1, 5):
    print(f"Person {i}:")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Sexo (M/F): ")

    names.append(name)
    ages.append(age)

    if gender.upper() == 'F':
        womans += 1

average_age = sum(ages) / len(ages)
older_index = ages.index(max(ages))
oldest_name = names[older_index]

print(f"Average age of the group: {average_age: .2f}")
print(f"Older: {oldest_name} (age: {max(ages)})")
print(f"number of women {womans}")


"""
Correção:

"""