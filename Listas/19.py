#19. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {}
dados['nome'] = str(input('Digite o nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 = não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = (int(input('Digite o ano de contratação: ')))
    dados['salario'] = (float(input('Informe seu salario em reais R$: ')))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)


for k,v in dados.items():
    print(f' - {k} tem valor igual {v}')

