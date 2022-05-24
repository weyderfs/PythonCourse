k = float(input("Quandos KM foram percorridos? "))
r = float(input("Qual o custo por KM rodado? R$"))
a = int(input("Por quantos dias foi alugado? "))
d = float(input("Qual o valor da diária? R$"))
c = k * r + a * d
print("O valor total a pagar é R${:.2f}".format(c))