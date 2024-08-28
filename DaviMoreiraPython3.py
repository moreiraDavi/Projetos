import math
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    def set_x(self,novo_x):
        if type(novo_x) == int:
            self.x = novo_x
        else:
            print("Dado computado incompatível.")

    def get_y(self):
        return self.y
    def set_y(self,novo_y):
        if type(novo_y) == int:
            self.y = novo_y
        else:
            print("Dado computado incompatível.")

    def distancia(self):
        calculo= math.sqrt((self.x-0)**2 + (self.y-0)**2)
        return calculo

    def distancia_dois_pontos(self,objeto2):
        calculo= math.sqrt((self.x-objeto2.x)**2 + (self.y-objeto2.y)**2)
        return calculo

    def mostra_mais_distante(self,objeto2):
        calculo = math.sqrt((self.x - 0) ** 2 + (self.y - 0) ** 2)
        calculo1= math.sqrt((objeto2.x - 0) ** 2 + (objeto2.y - 0) ** 2)
        if calculo > calculo1:
            print("O primeiro ponto e mais distante da origem que o segundo.")
        if calculo1 > calculo:
            print("O segundo ponto e mais distante da origem que o primeiro.")

    def __str__(self):
        dados= f'{self.x}, {self.y}'
        return dados


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(2,3)
    p3 = Point(x=3)
    p4 = Point(y=7)
    p1.set_x(33)
    p1.set_y(2)
    print("Objeto p1 da classe point:",p1)
    print("Objeto p1 da classe point:",p1.__str__())
    print("Objeto p2 da classe point:",p2.__str__())
    print("Objeto p3 da classe point:",p3.__str__())
    print("Objeto p4 da classe point:",p4.__str__())
    print(p2.distancia())
    print(p3.distancia())
    print(p2.distancia_dois_pontos(p3))
    p2.mostra_mais_distante(p3)