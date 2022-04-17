'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''
qtdPositivo = 0

#status da resposta (dicionário)
status = {2 : "Suspeito(a)",
            3 : "Cúmplice",
            4 : "Cúmplice",
            5 : "Assassino"}

#lista de perguntas
lista_perguntas = ["Telefonou para a vítima?",
                    "Esteve no local do crime?",
                    "Mora perto da vítima?",
                    "Devia para a vítima?",
                    "Já trabalhou com a vítima?"]
              
for i in range (0, len(lista_perguntas)):
    print(f'{lista_perguntas[i]} (sim ou não). ')
    resposta = input(str("Resp.: "))

    if resposta.lower() =="sim":
        qtdPositivo += 1


if qtdPositivo in status:
    print(status[qtdPositivo])
        
else:
    print ("Inocente")