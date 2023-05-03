"""
043: Desenvolva um script em python que leia o peso e a altura de uma pessoa, calcule seu índice de massa corporal (MC) e mostre seu status de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do peso; IMC entre 18,5 e 25: Peso ideal; IMC 25 até 30: Sobrepeso; IMC 30 até 40: Obesidade; IMC acima de 40: Obesidade Mórbida.
"""

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

imc = weight / (height ** 2)

if imc < 18.5:
    print("your IMC is {} and you are underweight.".format(imc))
elif 18.5 <= imc < 25:
    print("your IMC is {} and you are at your ideal weight.".format(imc))
elif 25 <= imc < 30:
    print("your IMC is {} and you are overweight.".format(imc))
elif 30 <= imc < 40:
    print("your IMC is {} and you are obese.".format(imc))
else:
    print("Your IMC is {} and you are morbidly obese.".format(imc))

"""
Correção:

"""