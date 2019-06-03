km = float(input('Quantos KMs o carro percorreu: '))
d = int(input('Quantos dias este carro ficou alugado? \n'))
r = km * 0.15
a = d * 60
print('O Valor total a ser pago pela locação do carro é  R${:.2f}'.format(r + a))
######Other forms
#km = float(input('Quantos KMs o carro percorreu: '))
#d = int(input('Quantos dias este carro ficou alugado? \n'))
#aluguel = (d * 60) + (km * 0.15)
#print('O Valor total a ser pago pela locação do carro é  R${:.2f}'.format(aluguel))