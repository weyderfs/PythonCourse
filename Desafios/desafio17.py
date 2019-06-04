from math import hypot

x = float(input('Informe o cateto X: '))
y = float(input('Informe o cateto Y: '))
print('A hipotenusa deste triângulo é {:.3f}'.format(hypot(x, y)))