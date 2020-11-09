


def calculaAreaRetangulo():
	
	x = input('Dê me de um a dois lados: ')
	y = input('Dê me de um a dois lados: ')

	area = 0
	x = int(x)

	if y == '':
		area = x*x

	else:
		y = int(y)
		area = x*y

	print(area)


print(calculaAreaRetangulo())