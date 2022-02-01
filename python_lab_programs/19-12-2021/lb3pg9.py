str1=input("enter a string")
length = len(str1)
if str1[-3:] == 'ing':
     str1 += 'ly'
     print(str1)
else:
     str1 += 'ing'
     print(str1)