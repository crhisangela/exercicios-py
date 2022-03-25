'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

metros = float(input("Quantos metros quadrdos deseja pintar?  "))
litro_por_metro = round(metros / 3 )
qtd_latas = round(litro_por_metro / 18)
valor = qtd_latas * 80

print(f"Para um espaço de {metros}m², é necessário {litro_por_metro}L de tinta, o recomendavél então é que compre {qtd_latas} latas de tinta, danto um valor total de {valor} reais")
