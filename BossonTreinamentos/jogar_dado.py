import random

class Dado:
    '''Classe Dado onde lança o dado'''
    def __init__(self):
        self.faces = (1, 2, 3, 4, 5, 6)
    def joga_dado(self):
        dado = random.choice(self.faces)
        return 'Resultado do dado: ' + str(dado)

lance = Dado().joga_dado()
print(lance)
print('Link da Aula: https://www.youtube.com/watch?v=C35cqd5N0h8&t=804')
