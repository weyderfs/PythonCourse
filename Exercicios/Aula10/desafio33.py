a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

# Verificando o menor
m = a

if b < a and b < c:
    m = b
if c < a and c < b:
    m = c

# Verificando o maior
M = a

if b > a and b > c:
    M = b
if c > a and c > b:
    M = c

print("Entre os valores digitados o menor é {:.1f} e o maior é {:.1f}".format(m, M))
