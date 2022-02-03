s1=input("Enter a string:")
if len(s1)> 2:
 if s1[-3:]=='ing':
    s1+='ly'
 else:
  s1+="ing"
print(s1)
