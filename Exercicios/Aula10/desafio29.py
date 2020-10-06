v = float(input('Qual a velocidade do carro? '))
m = (v - 80) * 7

if v <= 80:
    print('Boa viagem!!!! Dirija com segurança')
else:
    print('Você está acima do limite de velocidade de 80 KM/h e foi multado em R${:.2f}'.format(m))
