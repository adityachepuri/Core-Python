### WAP to find no.of occurences of each letter present in the given string ###

word = input("Enter some word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
print(sorted(d))
for k,v in sorted(d.items()):
    print("{} occured {} times".format(k,v))
