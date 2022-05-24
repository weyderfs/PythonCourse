n = str(input('Insira o seu nome completo: ')).strip()
x = n.split()

print(' ')
print('O nome inseiro foi: {}'.format(n.lower()))
print(' ')
print('Seu primeiro nome é: {}'.format(x[0]))
print(' ')
print('Seu último nome é: {}'.format(x[len(x) - 1]))
