# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

from defer import return_value


count = 0
lista = []

while count != 10:
    letras = str(input(f"Digite a {count + 1}º letra: "))
    lista.append(letras)
    count += 1

for l in lista:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        print(f'Você escolheu as vogais {l}')