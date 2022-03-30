'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3 para o Sindicato e que o FGTS corresponde a 11 do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valor_hora = float(input("Quanto você ganha por hora? R$ "))
qtd_horas = int(input("Quantas horas você trabalha no mês? "))

salario_bruto = (valor_hora * qtd_horas)
inss = salario_bruto  * 0.1
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    imposto = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    imposto = salario_bruto * 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500:
    imposto = salario_bruto * 0.1
elif salario_bruto > 1500:
    imposto = salario_bruto * 0.2

descontos = imposto + inss + fgts
salario_liquido = salario_bruto - descontos



print(f"Recebendo R$ {valor_hora} por hora em {qtd_horas}h no mês, seu salario bruto é de R$ {salario_bruto} \n Menos o imposto de renda de R$ {imposto} \n Menos o INSS de R$ {inss} \n Menos o fgts de R$ {fgts} \n Você possui um total de R${descontos} descontados do seu salário bruto, assim seu saĺario líquido é de R$ {salario_liquido} mensais")