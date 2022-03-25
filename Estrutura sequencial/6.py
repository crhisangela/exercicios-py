# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
math.pi

raio = float(input("Me informe o raio da circunfêrencia: "))

area = math.pi * (raio)**2

print(f"Para uma circunferência de raio {raio}, a área é de {area} m²")