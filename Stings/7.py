'''Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.'''

texto = input("Digite um texto: ").lower()

numero_espacos = texto.count(" ")
print(f'Tem {numero_espacos} espaços na frase')

vogais = ['a', 'e', 'i', 'o', 'u']

for v in vogais:
    cont_vogais = texto.count(v)
    print(str(v) + ": " + str(cont_vogais), end=" ")





