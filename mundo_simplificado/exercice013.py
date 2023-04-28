"""
013: Faça um algoritmo que leia o salário de um funcionário e moste seu novo salário, porém com 15% de aumento.
"""
current_wage = float(input("report your current salary: R$"))
increase = current_wage * 0.15
new_current_wage = current_wage + increase
print("Your current salary is {:.2f}".format(current_wage))
print("With the increase will be {:.2f}".format(new_current_wage))

"""
Correção:
salario = float(input("Qual é o salário do funcionário? R$ "))
novo = salario + (salario * 15 / 100)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salario, novo))

"""