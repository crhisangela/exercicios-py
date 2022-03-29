# 9 Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiro = float(input("Me diga um número. "))
segundo = float(input("Me diga outro um número. "))
terceiro = float(input("Me diga mais um número. "))

if primeiro > segundo > terceiro:
    print(f"A ordem crescente dos números é {primeiro}, {segundo}, {terceiro}")
elif segundo > primeiro > terceiro:
    print(f"A ordem crescente dos números é  {segundo}, {primeiro}, {terceiro}")
elif terceiro > segundo > primeiro:
    print(f"A ordem crescente dos números é {terceiro}, {segundo}, {primeiro}")
else:
    print("Números iguais!")