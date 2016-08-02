
# self em cada método é sempre necessário e é usado como uma refrencia interna a classe, para não ficar dúvidas
# do que está sendo chamado.

class Livro:

    # constructor (always init)
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    # metodo qualquer
    def imprime(self, nome = "Roberto"):
        print("%s pegou %s with %d" %(nome, self.title, self.isbn))


monge = Livro("O monge e o Executivo", 123456)
monge.imprime("Carlos")
print(type(monge))

pequeno_principe = Livro(isbn = 98765, title = 'O Pequeno Principe')
pequeno_principe.imprime("Carlos")


# Classe vazia
# Que recebe um objeto.

class Carro(object):
    pass


# Funções
print(hasattr(monge, "title"))
print(hasattr(monge, "salario"))

setattr(monge, "title", "O monge")
monge.imprime()

print(getattr(monge, "title", "sei lá"))
print(getattr(monge, "salario", "sei lá"))


class Circulo(object):
    pi = 3.14156

    def __init__(self, raio = 5):
        self.raio = raio

    def area(self):
        return self.raio**2 * Circulo.pi


# herança

class Animal(object):
    def __init__(self):
        print("Animal")

    def identifica(self):
        print("Animal - identifica")

    def comer(self):
        print("Animal - comer")

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro")

    def identifica(self):
        print("Cachorro - identifica")

    def latir(self):
        print("Cachorro - au au")

puppy = Cachorro()

puppy.identifica() # chama o overwritten

puppy.latir()

puppy.comer()


# metodos especiais
class Livro(object):
    def __init__(self):
        print("contructor")

    # when call str (or print e.g.)
    def __str__(self):
        return "Obj to String"

    # when call len(obj)
    def __len__(self):
        return 1

    # call when call del(obj, "attribute")
    # def __delattr__(self, item):
    # there are many special methods.https://www.facebook.com/#