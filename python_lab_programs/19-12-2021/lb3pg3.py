a=[]
n=int(input("enter the limit"))
sum=0
print("enter elements into the list")
for i in range(0,n):
    elem=int(input())
    a.append(elem)
print(a)
print("sum of elements in the list")
for elem in a:
	sum=sum+elem
print(sum)