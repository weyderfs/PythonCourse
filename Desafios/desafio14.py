t = float(input('Informe a temperatura em Celsius: '))
print('*'*15)
print('A temperatura em Fahrenheit corresponde a: {:.1f}F'.format((t * 9/5) + 32))
####Other Form
print('A temperatura em Fahrenheit corresponde a: {:.1f}F'.format(t * 9/5 + 32))