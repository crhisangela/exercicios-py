'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;'''

from re import I


qtd_valores = int(input('Quantas notas você quer analisar? '))
notas = []
maiorMedia = 0
maior7 = 0

for i in range(0, qtd_valores):
    notas.append(int(input(f'Qual a {i + 1}º nota? ')))
    if notas == -1:
        exit()

media = sum(notas) / len(notas)

for n in range(0, len(notas)):
    if notas[n] > media:
        maiorMedia += 1
    elif notas[n] > 7:
        maior7 += 1

print(f'Você escolheu trabalhar com {qtd_valores} notas')
print(notas)
print(notas[::-1])
print(f'Soma = {sum(notas)}')
print(f'Média = {media}')
print(f'Quantidade maior que a média = {maiorMedia}')
print(f'Quantidade maior que 7 = {maior7}')

