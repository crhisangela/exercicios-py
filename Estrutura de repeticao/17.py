# 17. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

n = int(input("Que N acima do 14 você gostaria de achar? "))
ultimo = 1
penultimo = 1


if (n <= 14):
    print("O valor precisa ser acima de 14 para que o programa mostre acima de 500")
else:
    print("0 \n1\n 1")
    for count in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo)
        count += 1
    print(termo)