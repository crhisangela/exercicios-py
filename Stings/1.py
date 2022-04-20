'''Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.'''

str1 = str(input("Digite a primeira frase: "))
str2 = str(input("Digite a segunda frase: "))

str1_len = len(str1)
str2_len = len(str2)

print(f'String 1: {str1}  \nString 2: {str2}')
print(f'Tamanho de "{str1}": {str1_len} caracteres \nTamanho de "{str2}": {str2_len} caracteres')

if str1_len == str2_len:
    print('As duas strings tem o mesmo tamanho.')
else:
    print('As duas strings tem tamanhos diferentes.')

if str1 == str2:
    print('As duas strings são iguais.')
else:
    print('As duas strings são diferentes.')

