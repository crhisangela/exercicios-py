'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''


a = float(input('Qual é o valo de a? '))

if (a==0):
    print('Se a é igual a zero a equação é inválida.')
else:
    b = float(input('Qual é o valo de b? '))
    c = float(input('Qual é o valo de c? '))
    delta = b*b - (4*a*c)


if delta < 0:
    print('Delta menor que 0 as raízes não existem.')
elif delta == 0:
    raiz = -b / (2*a)
    print(f'Delta = 0 , raiz = {raiz}')
else:
    raiz1 = (-b + (delta)**(1/2) ) / (2*a)
    raiz2 = (-b - (delta)**(1/2) ) / (2*a)
    print(f'Raizes: {raiz1} e {raiz2}')
