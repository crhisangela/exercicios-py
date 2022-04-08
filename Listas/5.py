#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
par = []
impar = []

for numero in range (0, 20):
    vetor.append(int(input(f'Me de um numero ({numero + 1} / 20): ')))

for numero in range (0, 20):
    if vetor[numero] % 2 ==0:
        par.append(vetor[numero])
    else:
        impar.append(vetor[numero])


print(f"Vetor com 20 elementos: {sorted(vetor)}" )
print(f"Vetor com elementos pares: {par} ")
print(f"Vetor com elementos i­mpares: {impar}")