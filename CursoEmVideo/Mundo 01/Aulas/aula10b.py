n1 = float(input('Insira a 1ª nota: '))
print(' ')
n2 = float(input('Insira a 2ª nota: '))
print(' ')

m = (n1 + n2) / 2
if m >= 6.0:
    print ('Sua média {:.1f} está AZUL continue assim e será aprovado.'.format(m))
else:
    print ('Sua média {:.1f} está VERMELHA estude mais para ser aprovado.'.format(m))

