l=[]
l1=[]
n=int(input("enter the limit of list"))
print("enter the elements in to the list")
for i in range(0,n):
    elem=input()
    l.append(elem)
print(l)
print("reversed list is")
for i in range(n-1,-1,-1):
  l1.append(l[i])
print(l1)



