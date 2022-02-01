l1=[]
n=int(input("enter a limit"))
print("enter the elements into the list")
for i in range(0,n):
    elem=int(input())
    if elem > 100:
     l1.append("over")
    else:
     l1.append(elem)
print(l1)