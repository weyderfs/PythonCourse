n = str(input('Insira o nome: ')).strip().upper()
l = str(input('Insira a letra que deseja contar no nome: ')).strip().upper()

print('O nome informado foi {}'.format(n))
print(' ')
print('A letra informada foi: {}'.format(l))
print(' ')
print('A letra {}, aparece {} vezes na frase.'.format(l, n.count(l)))
print(' ')
print('A primeira letra {} aparece na posição: {}'.format(l, n.find(l) + 1))
print(' ')
print('A última letra {}, aparece na posição {}'.format(l, n.rfind(l) + 1))

## Foi usado +1 para poder deixar a posição mais humana pois para o Python inicia na posição zero