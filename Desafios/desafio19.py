import random

n1 = input('Informe o primeiro nome: ')
n2 = input('Informe o segundo nome: ')
n3 = input('Informe o terceiro nome: ')
n4 = input('Informe o quarto nome: ')
print('O sorteado foi: {}'.format(random.choice([n1, n2, n3, n4])))