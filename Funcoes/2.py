'''Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.'''

def enesimo2(n):
    for i in range(1, n+1):
        for j in range(i):
            print(j, end=" ")
        print()

n = int(input('Escolha o seu enésimo termo: '))
print(enesimo2(n))
