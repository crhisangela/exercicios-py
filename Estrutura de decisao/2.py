# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero1 = float(input("Digite um número: "))

if numero1 < 0:
    print(f"{numero1} é negativo")
else:
    print(f"{numero1} é positivo")