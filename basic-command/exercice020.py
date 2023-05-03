"""
020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random
student1 = input("Enter the name of the first student: ")
student2 = input("Enter the name of the second student: ")
student3 = input("Enter the name of the third student: ")
student4 = input("Enter the name of the fourth student: ")
student_list = [student1, student2, student3, student4]
random.shuffle(student_list)
print("The order of presentation will be:")
print(student_list)

"""
Correção:

from random import shuffle
n1 = str(input"Primeiro aluno: "))
n2 = str(input"Segundo aluno: "))
n3 = str(input"Terceiro aluno: ")) 
n4 = str(input"Quarto aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação será:")
print(lista)
"""
