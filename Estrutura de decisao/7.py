# 7 Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro = float(input("Me diga um número. "))
segundo = float(input("Me diga outro um número. "))
terceiro = float(input("Me diga mais um número. "))

menor = primeiro

if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print(f'O menor número é o {menor}')