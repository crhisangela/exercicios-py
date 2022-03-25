"""Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""


inteiro1 = int(input("Me diga um número inteiro: "))
inteiro2 = int(input("Me diga outro numero inteiro: "))
real = float(input("Me diga um número real: "))

produto_segundo = inteiro1 * (inteiro2 / 2)
soma_triplo = (inteiro1 * 3) + real
cubo = real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é igual a {produto_segundo}")
print(f"A soma do triplo do primeiro com o terceiro é igual a {soma_triplo}")
print(f"O terceiro elevado ao cubo é igual a {cubo}")