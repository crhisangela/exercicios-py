# 10. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

cpf = input("CPF(xxx.xxx.xxx-xx) : ")

for v in cpf:
    if(cpf[3] !=".") or (cpf[7] !=".") or (cpf[11] !="-"):
        cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")
    else:
        print("O 'CPF' está no formato correto")