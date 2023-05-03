"""
045: Crie um script que faça o computador jogar Jokenpô com você.
"""

import random

player = input("Choose between Rock, Paper, Scissor: ")

options = ["Rock", "Paper", "Scissor"]
cpu = random.choice(options)

print("The player chose {}".format(player))
print("The CPU chose {}".format(cpu))

if player == cpu:
    print("Draw")
elif player == "Rock":
    if cpu == "Paper":
        print("CPU Win!")
    else:
        print("Player Win!")
elif player == "Paper":
    if cpu == "Scissor":
        print("CPU Win!")
    else:
        print("Player Win!")
elif player == "Scissor":
    if cpu == "Rock":
        print("CPU Win!")
    else:
        print("Player Win!")
else:
    print("Invalid move! Try again!")

"""
Correção:

"""