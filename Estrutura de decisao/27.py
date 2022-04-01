'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10 sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
maca =0
morango =0

kg_maca = int(input('Quantos kg de maça você vai comprar? '))
kg_morango = int(input('Quantos kg de morango você vai comprar? '))

if kg_maca <= 5:
    maca = 1.80
elif kg_morango <=5:
    morango = 2.50
else:
    maca = 1.50
    morango = 2.20

valor_maca = kg_maca * maca
valor_morango = kg_morango * morango

valor_total = valor_maca + valor_morango

peso_total = kg_maca + kg_morango

if peso_total > 8:
    valor_total = valor_total * 0.9

print(f'Em {peso_total} kg de maca e morango você pagará {valor_total} reais')
