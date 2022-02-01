a=input("enter a string")
c=a[0]
for i in a:
    first_letter=i
    break

for j in a:
    if(j==i):
     b=a.replace(first_letter,"$")
print(c+b[1:])