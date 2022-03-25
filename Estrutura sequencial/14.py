'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''


limite_peso = 50
peso_peixes = float(input("Qual o peso dos peixes de hoje? "))
multa = (peso_peixes - limite_peso) * 4
peso_sobrando = 50 - peso_peixes

if peso_peixes > limite_peso:
    print(f"O senhor excedeu o limite de peso, a multa a ser paga será de R${multa}.")
elif peso_peixes == limite_peso:
    print(f"O senhor está nos {limite_peso}kg de limite de peso.")
else:
    print(f'O senhor ainda pode pescar {peso_sobrando}kg de peixe hoje.')