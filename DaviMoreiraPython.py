class Pessoa:
    def __init__(self,nome="",dependente=0):
        self.nome= nome
        self.dependente= dependente


    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        self.nome=novo_nome


    def get_dependente(self):
        return self.dependente
    def set_dependente(self,novo_dependente):
        if novo_dependente >= 0:
            self.dependente = novo_dependente
        else:
            print('Erro')


    def __str__(self):
        return f'{self.nome}, {self.dependente}'


class Professor(Pessoa):

    def __init__(self,nome="",dependente=0,qtd_turma=0):
        super().__init__(nome, dependente)
        self.qtd_turma = qtd_turma


    def get_qtd_turma(self):
        return self.qtd_turma
    def set_qtd_turma(self,novo_qtd_turma):
        if novo_qtd_turma >= 0:
            self.qtd_turma= novo_qtd_turma
        else:
            print("Erro")


    def rendimento(self,valor):
        rend= valor*self.qtd_turma
        print(rend)

    def __str__(self):
        return f'{self.nome}, {self.dependente}, {self.qtd_turma}'


class Funcionario(Pessoa):

    def __init__(self,nome="",dependente=0,salario_fixo=0):
        super().__init__(nome,dependente)
        self.salario_fixo = salario_fixo


    def get_salario_fixo(self):
        return self.salario_fixo
    def set_salario_fixo(self,novo_salario_fixo):
        self.salario_fixo = novo_salario_fixo


    def salario_total(self):
        slr_total= (self.dependente*100) + self.salario_fixo
        print(f'O salario total de {self.nome} é: R${slr_total:.2f}')


    def __str__(self):
        return f'{self.nome}, {self.dependente}, {self.salario_fixo}'


if __name__ == '__main__':

    pessoa1 = Pessoa("Firmino", )
    professor1 = Professor('João',qtd_turma=9)
    funcionario1 = Funcionario(nome= "Carlos", dependente=5,salario_fixo=5000)

    print(funcionario1)

    print()

    funcionario1.salario_total()

    print()

    professor1.rendimento(500)