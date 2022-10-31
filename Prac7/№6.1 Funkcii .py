a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
Na,Nb = a,b
while Na != Nb:
	if Na>Nb:
		Na=Na-Nb
	else:
		Nb=Nb-Na
print('НОД =',Na)
print('НОК =',a*b//Na)		
