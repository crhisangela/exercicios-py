# 3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Qual o sexo? (F / M) ').upper()

if sexo == "F" or "FEM" or "FEMININO":
    print("F - Feminino")
elif sexo == "M" or "MASC" or "MASCULINO":
    print("M - Masculino")
else:
    print("Sexo inválido")