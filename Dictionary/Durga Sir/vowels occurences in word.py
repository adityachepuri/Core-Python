### WAP to fidn no.of vowels in the entered word ###

word = input("Enter some word:")
v={'a','e','i','o','u'}
d={}
for x in word:
    if x in v:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
  print("{} occured {} times".format(k,v))
