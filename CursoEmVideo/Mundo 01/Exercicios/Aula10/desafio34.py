s = float(input("Qual o salário? R$: "))
if s <= 1250:
    ns = s + (s * 15 / 100)
else:
    ns = s + (s *10 / 100)
print('Seu novo salario é R${:.2f}'.format(ns))