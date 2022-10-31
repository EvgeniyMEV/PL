import math
 
def s(p1, p2):
 form = math.sqrt(p1*(p1-a)*(p1-b)*(p1-f)) + math.sqrt(p2*(p2-d)*(p2-c)*(p2-f))
 return form
a=int(input('Введите длину стороны a: '))
b=int(input('Введите длину стороны b: '))
c=int(input('Введите длину стороны c: '))
d=int(input('Введите длину стороны d: '))
f=int(input('Введите длину стороны f: '))
 
p1=(a+b+f)//2
p2=(d+c+f)//2
 
print('Площадь = ',s(p1, p2))
