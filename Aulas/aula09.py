#Fatiamento de Cadeias de Strings
print('Técnica de Fatiamento de Caracteres')
frase = 'Curso em Vídeo Python'

print (frase[9])
print (frase[9:21])
print (frase[:5])
print (frase[15:])
print (frase[9::3])

#Análise de Caracteres
print('Técnicas de análise de caracteres')
len(frase)
frase.count('o')
frase.count('o', 0, 13)
frase.find('deo')
frase.find('Android')
print('Curso' in frase)

#Transformação
print('Transformando caracteres')
frase.replace('Python', 'Android')
frase.upper()
frase.lower()
frase.title()
frase.capitalize()

frase2 = print('   Aprenda Python   ')
frase2.strip()
frase2.rstrip()



