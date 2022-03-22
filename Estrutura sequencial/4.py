#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Qual a nota de Matematica? "))
nota2 = float(input("Qual a nota de Português? "))
nota3 = float(input("Qual a nota de Filosofia? "))
nota4 = float(input("Qual a nota de Artes? "))
media = ((nota1 + nota2 + nota3 + nota4) / 4)

print(f'A média geral do bimestre  foi {media}')
