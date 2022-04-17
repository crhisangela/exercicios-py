#12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


idade = []
altura = []
qtdAlunos = 0

for valor in range (0,7):
    idade.append(int(input(f"Digite a idade do {valor + 1}º aluno: ")))
    altura.append(float(input(f"Digite a altura do {valor + 1}º aluno: ")))

mediaAltura = sum(altura) / len(altura)

for i in range(0, len(idade)):
    if idade[i] > 13 and altura[i] < mediaAltura:
        qtdAlunos += 1

print (f"{qtdAlunos} alunos possuem mais de 13 anos e altura inferior a  media ({mediaAltura}) de altura dos alunos")