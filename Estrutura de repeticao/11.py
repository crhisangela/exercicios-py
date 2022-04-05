# 11. Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("digite um numero:  "))
n2 = int(input("digite outro numero:  "))

for i in range(n1 + 1, n2):
        print(i)

for i in range(n2 + 1, n1):
        print(i)

print("Soma dos números: ", i + i)