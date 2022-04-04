#Faça um programa que leia 5 números e informe o maior número.

cont = 0
lista_numeros =[]
while cont != 5: 
    numero = int(input('Digite um numero: '))
    lista_numeros.append(numero)
    cont = cont + 1

maior = max(lista_numeros)
print(f'O maior número escolhido foi o {maior}')