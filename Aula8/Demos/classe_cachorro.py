class Cachorro:
    
    def __init__(self, nome, idade, raca):
        self._nome = nome.title()
        self._idade = int(idade)
        self._raca = raca.title()

    def atualiza_nome(self, novo_nome):
        self.nome = novo_nome

    def atualiza_idade(self, novo_idade):
        self.idade = novo_idade

    def atualiza_raca(self, novo_raca):
        self.nome = novo_raca

    def informacoes(self):
        print(f'O cachorro da raça {self.raca} se chama {self.nome} e possui {self.idade} anos.')

    def sentar(self):
        print(f'O cachorro {self.nome} está sentado agora!')

    def rolar(self):
        print(f'O cachorro {self.nome} está rolando agora!')

    def deitar(self):
        print(f'O cachorro {self.nome} está deitado agora!')