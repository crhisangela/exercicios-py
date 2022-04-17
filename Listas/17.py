#17.  Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Qual o nome? '))
aluno['nota'] = float(input('Qual a nota? '))

if aluno['nota'] >= 7:
    aluno['situacao'] = 'aprovado'
elif aluno['nota'] == 5:
    aluno['situacao'] = 'recuperacao'
else:
    aluno['situacao'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')