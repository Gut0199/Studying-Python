"""
026: Faça um programa que leia uma frase pelo teclado e moste:
1º Quantas vezes a letra "A" aparece.
2º Em que posição ela aparece a primeira vez.
3º Em que posição ela aparece a última vez.
"""

phrase = input("Type a sentence: ")
qtd_a = phrase.upper().count('A')
first_position_a = phrase.upper().find('A')
last_position_a = phrase.upper().rfind('A')

print("The letter A appears {} several times in the sentence".format(qtd_a))
print("The first letter A appears in position {}".format(first_position_a + 1))
print("The last letter A appears in position {}".format(last_position_a + 1))

"""
Correção: 

frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase".format(frase.count('A')))
print("A primeira letra A apareceu na posição {}".format(frase.find('A')+1))
print("A última letra A apareceu na posição {}".format(frase.rfind('A')-1))

"""