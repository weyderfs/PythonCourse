#import math
###Adding perfomance import only library necessarie
from math import trunc

n = float(input('Insira um número real: '))
print('O número informado foi: {} e o seu inteiro é {}'.format(n, trunc(n)))

#####Without import
'''n = float(input('Insira um número real: '))
print('O número informado foi: {} e o seu inteiro é {}'.format(n, int(n)))'''

