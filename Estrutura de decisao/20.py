'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

nota1 = float(input("Qual a nota de Matematica? "))
nota2 = float(input("Qual a nota de Português? "))
nota3 = float(input("Qual a nota de Ed. Física? "))

media = round((nota1 + nota2 + nota3) / 3)

if media >= 7:
    print(f"Você está APROVADO com média {media}")
elif media < 7:
    print(f"Você está REPROVADO com média {media}")
elif media  == 10:
    print(f"Aprovado com Distinção com média {media}")
