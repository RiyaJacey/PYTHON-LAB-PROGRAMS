y={'carl':40,'alan':2,'bob':1,'danny':3}
l=list(y.items())
l.sort()
temp=dict(l)
print('Ascending order is',temp)

l.sort(reverse=True)
dict=dict(l)
print('Descending order is',dict)
