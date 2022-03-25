'''12 . Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

altura = float(input("Qual a sua altura em metros? "))
peso = (72.7 * altura) - 58

print(f"Para uma altura de {altura}m, o peso ideal seria {peso}kg")