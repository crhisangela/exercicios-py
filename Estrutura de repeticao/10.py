# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("digite um numero:  "))
n2 = int(input("digite outro numero:  "))

while n2 < n1:
    n1 = int(input("digite um numero:  "))
    n2 = int(input("digite outro numero:  "))
else:
	for i in range(n1,n2+1,1):
		print(i)