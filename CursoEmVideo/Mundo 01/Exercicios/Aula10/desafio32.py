from datetime import date

a = int(input('Qual ano deseja verificar? Se quiser o ano atual digite 0: '))

if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('o Ano {} é BISSEXTO'.format(a))
else:
    print('o Ano {} NÃO é BISSEXTO'.format(a))