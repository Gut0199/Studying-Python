"""
014: Escreva um program que converta uma temperatura digitada em Cº para Fº.
"""

temperature_C = float(input("Enter the temperature in Celsius: "))
temperature_F = (temperature_C * 1.8) + 32
print("{:.2f} degrees Celsius equals {:.0f} Fahrenheit".format(temperature_C, temperature_F))

"""
Correção:

C = float(input(" Informe a temperatura em ºC: "))
f = ((9 * C) / 5) +32
print("A temperatura de {}ºC corresponde a {}ºF".format(c, f))

"""