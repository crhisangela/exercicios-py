# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

count = 0
lista = []

while count != 10:
    numeros = float(input(f'Me de o {count + 1}º número: '))
    lista.append(numeros)
    count += 1

print('Decrescente: ', sorted(lista, reverse = True))