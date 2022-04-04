#8 Faça um programa que leia 5 números e informe a soma e a média dos números.

cont = 0
lista_numeros = []

while cont != 5:
    numero = int(input('Me de um número: '))
    lista_numeros.append(numero)
    cont = cont + 1


soma = sum(lista_numeros)
media = soma / cont

print(f'Dentre os valroes escolhidos a soma é {soma} e a média é {media}.')