# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.     C = 5 * ((F-32) / 9).

F = float(input("Qual a temperatura em Fahrenheit? "))
C = 5 * ((F-32) / 9)

print(f"{F} graus Fahrenheit equivalem a {C}ºC")