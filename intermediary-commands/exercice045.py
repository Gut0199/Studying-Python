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

from random import randint 

itens = ('pedra', 'papel', 'tesoura')
computador = radint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sau jogada? '))
print(f'Compuador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 3:
        print('Computador venceu!')
    else:
        print('Jogada Inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 3:
        print('Jogador Venceu!')
    else:
        print('Jogada Inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 3:
        print('EMPATE!')
    else:
        print('Jogada Inválida')

"""