#3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

count = 0
lista = []

while count != 4:
    notas = float(input(f'Qual a {count + 1}º nota? '))
    lista.append(notas)
    count += 1

media = sum(lista) / len(lista)

print(f'A média das notas é {media}')