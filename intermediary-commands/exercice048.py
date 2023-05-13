"""
Faça um script em Python que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo entre 1 a 500.
"""

sum = 0

for number in range(1, 501):
    if number % 2 != 0 and number % 3 == 0:
        sum += number

print("A soma dos números ímpares múltiplos de três é {}".format(sum))

"""
Correção:

"""