nome = str(input('Qual é o nome? '))
if nome == 'Luke':
   print('Eu sou seu pai!')
elif nome == 'Pedro' or nome == 'Jose' or nome == 'Paulo':
   print('Seu nome é bem comum no Brasil')
elif nome in 'Ana Claudia Maria Juliana':
   print('Seu nome é feminino')
else:
   print('Seu name é normal')
print('Have a nice day, {}!'.format(nome))
