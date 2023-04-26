print(5+3*2)
print(29//2)
print(19/2)
print(pow(4,3))
print(25**(1/2))
print(125**(1/3))
print('='*20)

nome = input('Qual teu nome? ')
print('Prazer {}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro Valor: '))

sm = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
dint = n1 //n2
exp = n1 ** n2
raiz = n1**(1/2)

print('A soma vale {} e a subtração {} '.format(sm, sb))
print('Multiplicação é {}, a divisão {} e o a divisão inteira {}'.format(m, d, dint ))
print('A potência {} e a raiz quadrada {}'.format(exp, raiz))