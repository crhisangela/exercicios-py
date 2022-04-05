# 13 Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('Qual a base? '))
expoente = int(input('Qual o expoente? '))

potencia=1

for count in range(expoente):
    potencia *= base
    count += 1

print(base,"^",expoente,"=",potencia)