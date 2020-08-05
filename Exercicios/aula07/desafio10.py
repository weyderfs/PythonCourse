m = float(input("Insira a quantia em BRL? R$"))
d = float(input("Qual o valor do Dólar? $"))
tx = m / d
print("O valor convertido da moeda é R${:.2f}".format(tx))