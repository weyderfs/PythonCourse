####FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES SOBRE ELA#####
x = input('Digite algo: ')
print('O Tipo primito é: ', type(x))
print('Não foi inserido nenhum caracter? ', x.isspace())
print('É um número inteiro? ', x.isnumeric())
print('É uma letra alfabética? ', x.isalpha())
print('É alfanumerico? ', x.isalnum())
print('Está maiúsculo? ', x.isupper())
print('Está tudo em minúsculo? ', x.islower())
print('Está capitalizado? ', x.istitle())