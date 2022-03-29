# 1Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}")
else:
    print(f"{numero2} é maior que {numero1}")