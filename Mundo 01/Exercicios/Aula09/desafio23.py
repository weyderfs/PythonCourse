num = int(input('Insira um número entre 0 e 9999: '))
# n = str(num)

# print("Analisando o Número {}".format(num))
# print("Sua Unidade é {}".format(n[3]))
# print("Sua Dezena é {}".format(n[2]))
# print("Sua Centena é {}".format(n[1]))
# print("O Milhar é {}".format(n[0]))

# O EXEMPLO ACIMA NÃO VALIDA QUANDO USADO MENOS DE 4 CHARS
# ABAIXO SEGUE MODELO MELHORADO
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o Número {}".format(num))
print("Sua Unidade é {}".format(u))
print("Sua Dezena é {}".format(d))
print("Sua Centena é {}".format(c))
print("O Milhar é {}".format(m))