# 22 Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = int(input('Me diga um número inteiro: '))

if numero % 2 ==0:
    print('O número escolhido é par.')
else:
    print('O número é impar')