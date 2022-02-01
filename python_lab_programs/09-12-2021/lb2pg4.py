a=[1,2,4,-1,-9,0,7]
b=[1,-2,-4,-1,9,0,7]
if(len(a)==len(b)):
    print("both list are of same length")
else:
    print("lists have different length")
if(sum(a)==sum(b)):
    print("both have same sum")
else:
    print("both have different sum values")
for i in a:
 for j in b:
    if(i==j):
        print(i,"present in both list")


