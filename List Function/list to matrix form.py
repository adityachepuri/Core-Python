x=[[10,20,30],[40,50,60],[70,80,90]]
for r in x:
 print(r)

print("Elements printed in matrix style:")
for i in range (len(x)):
    for j in range (len(x[i])):
      print(x[i][j], end=' ')
    print()
