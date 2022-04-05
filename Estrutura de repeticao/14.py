# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

cont = 0
lista =[[], []]
while cont != 10: 
    numeros = int(input('Digite um numero: '))
    if(numeros % 2 == 0):
        lista[0].append(numeros)
    else:
        lista[1].append(numeros)
    cont = cont + 1


print(f'Os números Pares digitados foram: {sorted(lista[0])}')
print(f'Os números Ímpares digitados foram: {sorted(lista[1])}')

