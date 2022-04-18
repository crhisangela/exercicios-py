# 9.	Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(*num):
    return str(num[::-1])

print(reverso(123,567,876))