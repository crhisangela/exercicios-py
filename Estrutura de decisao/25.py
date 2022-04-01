'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''


contador = 0
print("Responda as perguntas com S para sim ou N para não.")

p1 = input('Telefonou para a vítima? (s/n) ')
if p1 == 's':
    contador += 1


p2 = input('Esteve no local do crime? (s/n) ')
if p2 == 's':
    contador += 1


p3 = input('Esteve no local do crime? (s/n) ')
if p3 == 's':
    contador += 1


p4 = input('Mora perto da vítima? (s/n) ')
if p4 == 's':
    contador += 1


p5 = input('Devia para a vítima? (s/n) ')
if p5 == 's':
    contador += 1


if contador == 2:
    print('Suspeita')
elif contador == 3 or contador == 4:
    print('Cúmplice')
elif contador == 5:
    print('Assassino')
else:
    print('Inocente')