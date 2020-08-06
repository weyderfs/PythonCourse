s = float(input("Informe o salário do colaborador: R$"))
r = float(input("Qual a porcentagem do reajuste, informe apenas o número: "))
c = s + (s * r / 100)
print("Após o reajuste do salário informado R${}, ficou em R${}".format(s, c))
