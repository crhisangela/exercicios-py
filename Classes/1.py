'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor'''

class Ball:
    def __init__(self, color="unknown", circunference=0, material="unknown"):
        self.color = color
        self.circunference = circunference
        self.material = material

    def changeColor(self):
        change = (str(input('Deseja trocar de cor?[s/n]' ))).lower()

        if change == 's':
            newColor = str(input('Qual a nova cor? '))
            self.color = newColor
        else:
            print(f'Ok a cor continua sendo {self.color}')

    def isColor(self):
            print(f'A cor é {self.color}')

def main():
    bola01 = Ball("azul", 5, "metal")

    while True:
        bola01.changeColor()
        bola01.isColor()

        continuee = (input("Continuar? [s/n]")).lower()

        if continuee == "n":
            break

main()
