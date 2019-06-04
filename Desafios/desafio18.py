import math

print('Calculando seno, cosseno e tangente!')
ang = float(input('Digite o ângulo desejado: '))
print('O ângulo de {}, possui:\nSENO: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))
