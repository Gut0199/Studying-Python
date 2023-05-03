"""
037: Escreva um script em python que leai um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para o binário, 2 para o octal e 3 para hexadecimal.
"""

num = int(input("Enter an integer"))
print("Choose concession basis:")
print("[1] - Binary")
print("[2] - Octal")
print("[3] - Hexadecimal")
option = int(input("your option:: "))

if option == 1:
    print("{} converted to binary is equal to {}".format(num, bin(num)[2:]))
elif option == 2:
    print("{} converted to octal is equal to {}".format(num, oct(num)[2:]))
elif option == 3:
    print("{} converted to hexadecimal is equal to {}".format(num, hex(num)[2:]))
else:
    print("Invalid option!")

"""
Correção:

"""