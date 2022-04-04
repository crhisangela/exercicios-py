# 5 Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.



A = int(input('Qual o número total da população A (menor população) '))
taxaA = float(input('Qual a taxa de crescimento anual da população A? '))

B = int(input('Qual o número total da população B (maior população) '))
taxaB = float(input('Qual a taxa de crescimento anual da população B? '))

anos = 0
while A < B:
    A = A + (A * (taxaA/100))
    B = B + (B * (taxaB/100))
    anos = anos + 1

print(f'Serão necessários {anos} anos para que a população de A ultrapasse B')