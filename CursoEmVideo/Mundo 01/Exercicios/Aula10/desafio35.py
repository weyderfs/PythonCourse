r1 = float(input('Insira a primeiro segmento: '))
r2 = float(input('Insira o segundo segmento: '))
r3 = float(input('Insira o Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Com estes valores os segmentos formam o triângulo!')
else:
    print('Os segumentos não formam o triângulo com estes valore!')