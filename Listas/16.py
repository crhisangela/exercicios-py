#16. Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está usando como valor.

pessoas = { "Crhis": "Rosa", "Ruth": "Preto", "João": "Cinza", "Alecs": "Marrom", "Paula": "Preto" }

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

#####com input
pessoas = list()
valores = dict()

for p in range (0,5):
    valores['Nome'] = str(input('Qual o nome da pessoa? '))
    valores['Cor da camisa'] = str(input('Qual a cor da camiseta? '))
    pessoas.append(valores.copy())

for p in pessoas:
    print(p)