p = float(input("Qual o preço do produto? R$"))
d = float(input("Insira o valor do desconto apenas o número: "))
c = p - (p * d / 100)

print("O valor final é R${:.2f}".format(c))

