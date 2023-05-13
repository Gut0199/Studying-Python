"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 a 0 com uma pausa de 1 segundo.
"""

from time import sleep

counter = 10

while counter >= 0:
    print(counter)
    sleep(2)
    counter -= 1

print("Estouro de fogos de artifícios!")

"""
Correção:

"""