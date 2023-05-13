"""
Crie um script que leia uma frase qualquer e diga se ela é um palindromo, porém desconsiderando os espaços.
"""


def eh_palindromo(phrase):
    phrase = phrase.replace(" ", "")
    phrase_inverted = phrase[::-1]

    return phrase.lower() == phrase_inverted.lower()


phrase = input("Type a sentence: ")

if eh_palindromo(phrase):
    print("The sentence is a palindrome.")
else:
    print("The sentence is't a palindrome.")

"""
Correção:

"""
