print('Soma:',5+2)
print('Subtração:',5-2)
print('Multiplicação:',5*2)
print('Divisão Real:',5/2)
print('Potênciação:',5**2)
print('Divisão inteira:',5//2)
print(5%2)
print('='*50)
########Ordem de Precedência
#1 -> () em python não se usa chaves ou colchetes, apenas parenteses.
#2 -> **
#3 -> * / // %
#4 -> + -
#########
print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)
print('Potencia usando a função pow:',pow(4,3))
print('Raíz quadrada:',(81**(1/2)))
print('Raiz cúbica:',81**(1/2))
print('Oi'+ 'Ólá')
nome = str(input('Qual seu nome?'))
print('Testando alinhamento {:=^20}'.format(nome))
print('='*50)
#########
n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))