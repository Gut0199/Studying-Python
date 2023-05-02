"""
034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, o aumento será de 10%. Já para salários inferiores ou iguais, o aumento é de 15%.
"""

salary = float(input("Enter the employee's salary: "))

if salary > 1250:
    increase = salary * 0.10
else:
    increase = salary * 0.15

new_salary = salary + increase

print("The new salary is: {}")

"""
Correção:

salario = float(input("Qual é o salário do funcionário? R$"))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print("Quem ganhava R${:.2f} passou a ganhar R${:.2f}".format(salario, novo))

"""