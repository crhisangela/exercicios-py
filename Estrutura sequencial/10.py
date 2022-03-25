# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


C = float(input("Qual a temperatura em graus Celsius? "))
F = (C - 32) * (5 / 9)

print(f"{C} graus Celsius equivalem a {F} graus Fahrenheit.")
