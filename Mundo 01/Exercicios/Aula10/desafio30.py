from time import sleep

n = int(input('Digite um número inteiro: '))
r = n % 2

sleep(2)

if r == 0:
    print ('O número {} é PAR'.format(n))
else:
    print('O número {} é IMPAR'.format(n))