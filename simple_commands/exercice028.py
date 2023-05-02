"""
028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint

number = randint(0, 5)

print("Try to guess the number I'm thinking of between 0 to 5...")
guess = int(input("What's your guess?: "))

if guess == number:
    print("Congratulations! You're right")
else:
    print("What a shame! You missed.")

"""
Correção:

from random import randint
from time import sleep

computador = randint(0, 5)
print("=="*20)
print("Vou pensar em um número entre 0 à 5. Tente adivinhar.")
print("=="*20)
jogador = int(input("Em qeu número eu pensei? ")
sleep(2)
if jogador == computador:
    print("Parabéns! Você venceu!")
else:
    print("Vish! Eu ganhei!")

"""