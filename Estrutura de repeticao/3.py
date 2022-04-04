'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

#Nome: maior que 3 caracteres;

nome = str(input('Digite seu nome. '))
while (len(nome) < 3 ):
    nome = str(input('Digite seu nome. '))


#Idade: entre 0 e 150;

idade = int(input('Digite sua idade '))
while (idade < 0) or (idade > 150):
    idade = int(input('Digite sua idade '))


# Salário: maior que zero;

salario = float(input('Digite seu salário '))
while (salario < 0):
    salario = float(input('Digite seu salário '))


# Sexo: 'f' ou 'm';

sexo = str(input('Digite seu sexo (f/m) '))
while (sexo != 'f') and (sexo != 'm'):
    sexo = str(input('Digite seu sexo (f/m) '))


#Estado Civil: 's', 'c', 'v', 'd';'''

estado_civil = str(input('seu estado civil: (s)SOLTEIRO, (c)CASADO, (v)VIUVO, (d)DIVORCIADO ')).lower
while ( estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d" ):
    estado_civil = str(input('seu estado civil: (s)SOLTEIRO, (c)CASADO, (v)VIUVO, (d)DIVORCIADO ')).lower
