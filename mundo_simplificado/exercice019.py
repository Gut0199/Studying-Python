"""
019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do aluno escolhido.
"""

import random
student1 = input("Enter the name of the first student: ")
student2 = input("Enter the name of the second student: ")
student3 = input("Enter the name of the third student: ")
student4 = input("Enter the name of the fourth student: ")
student_list = [student1, student2, student3, student4]
chosen_student = random.choice(student_list)
print("The student chosen to erase the board was: ", chosen_student)

"""
Correção:

from random import choice
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista_alunos = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O aluno escolhido foi{}".format(escolhido))
"""