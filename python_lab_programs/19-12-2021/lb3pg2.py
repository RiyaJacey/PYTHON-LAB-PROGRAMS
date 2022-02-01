n=int(input("enter a limit"))
n1=0
n2=1
print("fibonacci series is\n",n1,"\n",n2)
for i in range(1,n):
 n3=n1+n2
 n1=n2
 n2=n3
 print("\n",n3)