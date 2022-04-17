#8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida


idade = []
altura = []

for valor in range (0,5):
    idade.append(int(input("Digite a idade: ")))
    altura.append(float(input("Digite a altura: ")))

print('Idade ordem inversa')
for valor in range(0,5):
    print(idade[len(idade)-1-valor])


print("Alturas na ordem inversa: ")
for valor in range(0, 5):
    print(altura[len(altura)-1-valor])