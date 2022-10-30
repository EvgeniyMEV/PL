N=10
a=[]
for i in range(N):
	x=int(input())
	a.append(x)
print(a)
s =0
for i in range(N):
	if a[i]>5:
		s=s+a[i]
g = int()
h = int()
for i in range(N):
	f=max(a)
	if a[i]<f:
		g +=1
	if a[i]>f:
		h +=1	
print('Сумма элементов >5: ',s)
print('Максимальный элемент: ',f)
print('Кол-чо элементов < максимального: ',g)
print('Кол-чо элементов > максимального: ',h)

	 		
	
