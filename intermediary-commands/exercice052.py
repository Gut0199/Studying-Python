"""
Faça um script em Python que leia um número inteiro e diga se ele é ou não um número primo.
"""


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


numbers = int(input("Enter the whole number: "))

if is_prime(numbers):
    print("The number is prime!")
else:
    print("The number is not prime!")


"""
Correção:

"""