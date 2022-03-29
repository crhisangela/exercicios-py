# 6 Faça um Programa que leia três números e mostre o maior deles.

primeiro = float(input("Me diga um número. "))
segundo = float(input("Me diga outro um número. "))
terceiro = float(input("Me diga mais um número. "))

maior = primeiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

print(f'O maior número é o {maior}')