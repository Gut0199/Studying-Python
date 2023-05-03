"""
040: Crie um script que leia duas notas de uma aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0 REPROVADO; Média entre 5.0 e 6.9 RECUPERAÇÃO; Média 7.0 ou superior APROVADO.
"""

note1 = float(input("Enter the first note: "))
note2 = float(input("Enter the second note: "))

media = (note1 + note2) / 2

if media < 5.0:
    print("Average: {}; DISAPROVED.")
elif 5.0 >= media <= 6.9:
    print("Averange: {}; RECOVERY.")
else:
    print("Averange: {}; APPROVED.")

"""
Correção:

"""