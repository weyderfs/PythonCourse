from random import randint
from time import sleep

t = randint(0, 5) #Randomiza um número dentro do range informado.
print(' ')
print('#£#' * 20)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar')
print('#£#' * 20)
print(' ')
n = int(input('Insira um número inteiro entre 0 & 5: ')) #O Jogador tentar adivinhar
print('PROCESSANDO.....@@@@@@')
sleep(3)

if n == t:
    print('SHOW, você é adivinhador!!!!')
else:
    print('Errou, eu pensei outro número {}'.format(t))
        


