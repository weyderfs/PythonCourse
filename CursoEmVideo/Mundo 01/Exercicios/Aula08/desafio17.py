#import math
from math import hypot

co = float(input("Insira o Cateto oposto do Triângulo retângulo: "))
ca = float(input("Insira o Cateto adjacente do Triângulo retângulo: "))

#h = (co ** 2 + ca ** 2) ** (1/2)
#h = math.hypot(co, ca)
h = hypot(co, ca)

print("A hipotenusa é: {:.2f} ".format(h))
