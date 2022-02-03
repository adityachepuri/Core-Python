###

word=input("Enter some word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
