

frase = str(input('Insira uma frase: '))
frase = frase.upper()

x = str(input('Insira a letra a buscar: '))
x = x.upper()

vogais = ['A','E','I','O','U']
vogal = list(filter(lambda i: i in frase, vogais))

consoantes = ['B','C','D','E','F','G','H','J','K',
'L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
consoante = list(filter(lambda i: i in frase, consoantes))

numeros = ['1','2','3','4','5','6','7','8','9','0']
numero = list(filter(lambda i: i in frase, numeros))

# Falta fazer o finder funcionar !!!!!! 

#finder = lambda x: True if x in frase


### TEST ###

print(vogal, consoante, numero)