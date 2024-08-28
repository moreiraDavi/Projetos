from abc import ABC, abstractmethod
class Carro(ABC):

    quantidade_instanciada = 0
    preco_base = 100

    @classmethod
    def get_quantidade_instanciada(cls):
        return cls.quantidade_instanciada

    @classmethod
    def get_preco_base(cls):
        return cls.preco_base

    @classmethod
    def set_preco_base(cls, novo_valor):
        cls.preco_base = novo_valor

    def __init__(self, modelo):
        self.modelo = modelo
        Carro.quantidade_instanciada += 1

    def __init__(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    @abstractmethod
    def preco_diario(self):
        pass

class Economica(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)

    def preco_diario(self):
        val_diaria = Carro.get_preco_base() *1.05
        return val_diaria

class Intermediario(Carro):
    def __init__(self,modelo):
        super().__init__(modelo)

    def preco_diario(self):
        val_diario = Carro.get_preco_base() * 1.10
        return val_diario


if __name__ == '__main__':
    carro1 = Economica("celta")
    print(carro1.get_modelo(), carro1.preco_diario())

    carro2 = Intermediario("onix")
    print(carro2.get_modelo(), carro2.preco_diario())

    carro3 = Intermediario("kwid")
    print(carro3.get_modelo(), carro3.preco_diario())
    print(Carro.quantidade_instanciada)