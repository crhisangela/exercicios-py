'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''


a = float(input('Me diga o tamanho do lado A do triângulo: '))
b = float(input('Me diga o tamanho do lado B do triângulo: '))
c = float(input('Me diga o tamanho do lado CA do triângulo: '))

if (a == b) and (a == c):
    print('Esse é um Triângulo Equilátero')
elif (a == b) or (a == c) or (b == c):
    print('Esse é um Triângulo Isósceles')
elif (a + b < c) or (a + c < b) or (b + c < a):
    print('Não é um triângulo')
else:
    print('Esse é um Triângulo Escaleno')
  