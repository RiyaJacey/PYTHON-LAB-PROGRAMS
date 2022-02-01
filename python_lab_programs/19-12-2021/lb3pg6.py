import math
a=int(input("enter a limit"))
l=[]
print("enter 4 digit nos into the list with each digits in a number as even")
for i in range(0,a):
	e=int(input())
	l.append(e)
print(l)
for e in l:
  	root = math.sqrt(e)
  	if int(root + 0.5) ** 2 == e:
  		print(e, "is a perfect square")
  	else:
  		print(e,"is not a perfect square")