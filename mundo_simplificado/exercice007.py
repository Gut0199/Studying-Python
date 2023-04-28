"""
007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

grade_note1 = float(input("Please inform the student's first grade: "))
grade_note2 = float(input("Please inform the student's second grade: "))
grade_average = (grade_note1 + grade_note2) / 2
print("The average for this student will be {}.".format(grade_average))