"""
Desenvolva um script em Python que leia o Primeiro Termo e a Razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

first_term = int(input("Please enter the first form of the PA: "))
reason = int(input("Please enter the reason of the PA: "))

print("The first 10 terms of the AP are:")

for i in range(10):
    term = first_term + i * reason
    print(term)

"""
Correção:

"""