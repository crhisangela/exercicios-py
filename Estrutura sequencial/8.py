#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Quanto você ganha por hora? R$ "))
qtd_horas = int(input("Quantas horas você trabalha no mês? "))

salario = valor_hora * qtd_horas

print(f"Recebendo R$ {valor_hora} por hora em {qtd_horas} no mês, seu saĺario é de R$ {salario} mensais")