"""
Faça um script em Python que leia seis números inteiros e mostre na tela a soma apenas daqueles que forem pares. Se o valor digitado for impar deve-se desconsiderá-lo.
"""

sum = 0

for i in range(6):
    number = int(input("Please enter an integer: "))

    if number % 2 == 0:
        sum += number

print("The sum of even numbers is {}".format(sum))


"""
Correção: 

"""