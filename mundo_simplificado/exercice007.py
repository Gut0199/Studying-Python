"""
007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

grade_note1 = float(input("Please inform the student's first grade: "))
grade_note2 = float(input("Please inform the student's second grade: "))
grade_average = (grade_note1 + grade_note2) / 2
print("The average for this student will be {}.".format(grade_average))

"""
Correção:
n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
media = (n1 + n2) / 2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}.".format(n1, n2, media))

"""