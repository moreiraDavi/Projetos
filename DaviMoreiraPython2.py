import datetime
class Pessoa:
    def __init__(self,nome,peso,altura,anoDeNascimento=2000):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.anoDeNascimento = anoDeNascimento

    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        if isinstance(novo_nome,str):
            self.nome = novo_nome
        else:
            print("Tipo de informação invalida.")

    def get_peso(self):
        return self.peso
    def set_peso(self,novo_peso):
        self.peso = novo_peso

    def get_altura(self):
        return self.altura
    def set_altura(self, novo_altura):
        self.altura = novo_altura

    def get_anoDeNascimento(self):
        return self.anoDeNascimento
    def set_anoDeNascimento(self, novo_anoDeNascimento):
        self.anoDeNascimento = novo_anoDeNascimento

    def mostra_dados(self):
        print("Nome: ",self.nome)
        print("Peso: ",self.peso," Kg")
        print("Altura: ",self.altura," M")
        print("Ano de Nascimento: ",self.anoDeNascimento)

    def __str__(self):
        dados = f'{self.nome}, {self.peso}, {self.altura}, {self.anoDeNascimento}'
        return dados
    def calcular_imc(self):
        print( self.peso/ (self.altura**2))
    def calcular_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.anoDeNascimento
        return idade

if __name__ == '__main__':
    pessoa1 = Pessoa("Davi Moreira",80,1.80,2005)
    pessoa1.mostra_dados()
    pessoa2 = Pessoa("Joaozinho",99,1.87,2000)
    print()
    pessoa2.mostra_dados()
    pessoa2.set_nome(1223)
    pessoa2.calcular_imc()
    print(pessoa2.__str__())
    print(pessoa2.calcular_idade())

