from random import shuffle

n1 = input('Insira um nome: ')
n2 = input('Insira um nome: ')
n3 = input('Insira outro nome: ')
n4 = input('Insira mais um nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('O escolhido foi: {}'.format(lista))