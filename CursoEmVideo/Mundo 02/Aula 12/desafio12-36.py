# Escreva um programa para aprovar o emrpéstimo bancário para compra de uma casa.

# O Programa deverá perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do saário ou então o empréstimo será Negado

casa = float(input('Valor do Imóvel: R$ '))
renda = float(input('Valor da sua renda mensal: R$ '))
tempo = int(input('Quantos anos de financiamento? '))
parcela = casa / (tempo * 12)
corte = renda * 30 / 100

if parcela <= corte:
   print('Empréstimo APROVADO!')
else:
   print('Empréstimo REPROVADO!')

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, tempo), end =' ')
print('a parcela será de R${:.2f}'.format(parcela))
print('Comparando tem que pagar {} e o mínimo é de {}'.format(parcela, corte))