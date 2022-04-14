# 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0


mais7 = []

for valor in range (0,4):    
    notas = (int(input(f'Qual a {valor + 1}º nota? ')))
    if notas >= 7:
        mais7.append(notas)    
    

print(f'As médias maior que 7 são {mais7}')