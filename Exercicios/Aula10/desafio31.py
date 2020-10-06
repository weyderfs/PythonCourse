v = float(input('Qual a distância em KM da viagem? '))

if v <= 200:
    print('O total da sua viagem fica em R${:.2f}'.format(v * 0.5))
else:
    print('O total da sua viagem fica em R${:.2f}'.format(v * 0.45))

#Another method

''' 
if v <= 200:
    p = v * 0.5
else:
    p = v * 0.45

print('O valor da sua passagem é {}'.format(p))
''' 