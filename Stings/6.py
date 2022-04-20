'''Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.'''

dia, mes, ano = input('Data (dd/mm/aaaa): ').split('/')

meses = ['janeiro','fevereiro','março','abril',
         'maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro']

print (f'Você nasce em: {dia} de {meses[int(mes)-1]} de {ano}')

