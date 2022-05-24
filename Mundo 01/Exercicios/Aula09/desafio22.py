n = str(input("Insira seu Nome: ")).strip()

print("Seu nome em maiusculo é {}".format(n.upper()))
print("Seu nome em maiusculo é {}".format(n.lower()))
print("Seu nome possui {} caracteres".format(len(n) - n.count(' ')))
print("Seu primeiro nome tem {} letras".format(n.find(' ')))

separa = n.split()
print("Seu primeiro nome é {} ele tem {} letras".format(separa[0], len(separa[0])))