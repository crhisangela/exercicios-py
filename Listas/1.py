# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

count = 0
lista = []

while count != 5:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    count += 1

print('Crescente: ', sorted(lista))