'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3 por litro
acima de 20 litros, desconto de 5 por litro
Gasolina:
até 20 litros, desconto de 4 por litro
acima de 20 litros, desconto de 6 por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

alcool = 1.90
gasolina = 2.50

combustivel = str(input('Qual combustivel você deseja? A-álcool, G-gasolina ')).lower
litros = int(input('Quantos litros você deseja? '))


if combustivel == 'a':
    combustivel = alcool
    if litros <= 20:
        desconto = combustivel * 0.97
        valor = litros * combustivel
    else:
        desconto = combustivel * 0.95
        valor = litros * combustivel
else:
    combustivel = gasolina
    if litros <= 20:
        desconto = combustivel * 0.96
        valor = litros * combustivel
    else:
        desconto = combustivel * 0.94
        valor = litros * combustivel


print(f'Em {litros} litros de combustivel você pagará {valor} reais, tendo {desconto} reais de desconto.')
