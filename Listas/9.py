#9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetorA = []
soma = []

for valor in range (0,10):
    vetorA.append(int(input('Digite um número: ')))
    soma = soma + (vetorA[len(vetorA)-1]**2)

print(f'A soma dos quadrados dos valores são {soma}')