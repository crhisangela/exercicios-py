#8.	Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contador(n):
    return len(str(n))

num = int(input('Digite um grande valor inteiro: '))

print(f'no valor escolhido tem {contador(num)} numeros inteiros')