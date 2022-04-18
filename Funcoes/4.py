#4.	Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def pos_neg(n=0):
    if n >= 0:
        return "P"
    else:
        return "N"

num = float(input('Digite um número: '))

print(pos_neg(num))