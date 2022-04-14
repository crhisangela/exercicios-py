# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = []
soma = 0
multip = 0

for numero in range (0,5):    
    lista.append(int(input(f'Qual a {numero + 1}º numero? ')))

for n in lista:
    multip *= n
    soma += n


print(f'A soma de {lista} é igual a {soma} e a multiplicação é igual a  {multip}.')