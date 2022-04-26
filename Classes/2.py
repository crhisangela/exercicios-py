'''Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''


class Square:
    def __init__(self, side="0"):
        self.side = side
    
    @property
    def side(self):
        return self.__side

    @side.setter
    def side (self, valor):
        if valor.isdigit():
            self.__side = valor
        else:
            print("O valor do lado deve ser apenas em numeros")

    def valueSIDE(self):
        print("\nO valor do lado é {} cm".format(self.__lado))

    def changeSIDE(self):
        newSide = input("\nMudar lado de {} cm para: ".format(self.__lado))
        self.lado = newSide

    def area(self):
        print("\nA área do quadrado é {:.2f} cm²".format(
            float(self.__lado) * float(self.__lado)))

    def calcArea(self):
        print("\nA área do quadrado é {:.2f} cm²".format(
            float(self.__lado) * float(self.__lado)))

    def __str__(self):
        return "O quadrado possui {} cm de lado e {:.2f} cm² de area".format(
            self.__lado, float(self.__lado) * float(self.__lado))



def main():
    quadradoA = Square()
    lado = input("Insira o valor do lado: ")
    quadradoA.lado = lado

    print(quadradoA)

    quadradoA.changeSIDE()
    quadradoA.valueSIDE()
    quadradoA.calcArea()


main()