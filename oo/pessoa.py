class Pessoa:
    def __init__(self, param_nome = None, idade=35):   # se usa __init__ para criar atributos de objetos ou instancias
        self.idade = idade     # adicionado com Alt Enter no PyCharm
        self.nome = param_nome # usando 'param_nome' (no lugar de nome como na aula) para distinguir:
                               # ATRIBUTO nome (self.nome) de PARAMETRO nome (param_nome)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Arthur')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
##    print(p.cumprimentar(7)) # aceita só um argumento posicional - p já se passa como argumento
    print(p.nome)
    p.nome = 'Marcelo'
    print(p.nome)