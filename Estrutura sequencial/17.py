'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10 de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''


metros = float(input("Quantos metros quadrdos deseja pintar?  "))

litro_por_metro = round(metros / 6 )


### LATAS
latas = (litro_por_metro / 18)
if latas % 18 != 0:
    latas += 1
valor_latas = latas * 80


##GALOES
galoes = litro_por_metro / 3.6

if galoes % 3.6 != 0: 
    galoes += 1
valor_galoes = galoes * 25

##MISTURAS
mistura_lata = round(litro_por_metro / 18)
mistura_galoes = round(litro_por_metro - (mistura_lata *18) / 3.6 )

if litro_por_metro - (mistura_lata * 18) % 3.6 != 0:
    mistura_galoes += 1
galoes_total = (mistura_lata * 80) + (mistura_galoes * 25)



print(f"Total de Litros necessário para pintar: {litro_por_metro}L. \n Apenas latas de 18 litros: {latas} Und. - Preço: R$ {valor_latas} \n Apenas galões de 3.6 litros: {galoes} Und. - Preço: R$ {valor_galoes} \n Mistura: {mistura_lata} Latas e {mistura_galoes} Galões = R$ {galoes_total}")
