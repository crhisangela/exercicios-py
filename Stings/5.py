'''Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F'''

nome = str(input("Digite um nome: ")).upper()
cont = 0

for i in range(0, len(nome) + 1):
    print(nome[i:])
