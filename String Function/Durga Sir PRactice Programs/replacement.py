####################################
s="aditya a good boy"
s1=s.replace("good", "bad")
print(s1,"Address of s1:", id(s1))
print(s,"Address of s:", id(s)) # Even replace operator also cannot change the object, as string is immutable
######################################

s="aabbaabbaabbaabb"
print(id(s))
s=s.replace("a","b")
print(s, id(s))
