'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

numero1 = float(input('Me de um número. '))
numero2 = float(input('Me de outro número. '))

print('Que operação deseja? ')

operacao = int(input('1 - Soma\n2 - Subtração\n3- Multiplicação\n4 - Divisão \n'))

if operacao == 1:
    result = numero1 + numero2
elif operacao == 2:
    result = numero1 - numero2
elif operacao == 3:
    result = numero1 * numero2
elif operacao == 4:
    result = numero1 / numero2
else:
    print('Opção invalida')


print(f'Resultado = {result}')

if result % 2 == 0:
    print('Valor positivo')
else:
    print('Valor negativo')

if result >= 0:
    print('Número positivo')
else:
    print('Número negativo')

if type(result) == int:
    print('Número inteiro')
else:
    print('Número decimal')