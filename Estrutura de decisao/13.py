'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''


dia_semana = int (input("Me de um dia da semana em número (1-Domingo, 2- Segunda, etc). "))


if dia_semana == 1:
    print("Você escolheu domingo")
elif dia_semana == 2:
    print("Você escolheu segunda")
elif dia_semana == 3:
    print("Você escolheu terça")
elif dia_semana == 4:
    print("Você escolheu quarta")
elif dia_semana == 5:
    print("Você escolheu quinta")
elif dia_semana == 6:
    print("Você escolheu sexta")
elif dia_semana == 7:
    print("Você escolheu sabado")
else:
    print('Valor inválido')
