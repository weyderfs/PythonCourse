c = float(input("Informe a temperatura em Celsius: "))
#Olha a ordem de precedencia operando no cálculo abaixo
f = 9 * c / 5 + 32
k = c + 273
print("{}°C em Farenheit é {}F".format(c, f))
print("{}°C em Farenheit é {}K".format(c, k))