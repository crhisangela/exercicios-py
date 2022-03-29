# 8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

primeiro = float(input("Me diga o valor do primeiro produto. "))
segundo = float(input("Me diga o valor do segundo produto. "))
terceiro = float(input("Me diga o valor do terceiro produto. "))

menor = primeiro

if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print(f'Você deve comprar o produto de {menor} reais')