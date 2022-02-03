### WAP to find unique no.of vowels and consonants present in the intended word ###

vowels=['a','e','i','o','u']
word=input("Enter some word:")
found=[]
consonants=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
    else:
        consonants.append(letter)
print("Total vowels in entered",word,"are:",found)
print("The no.of different vowels present in",word,"is:",len(found))
print()
print("Total consonants in entered",word,"are:",consonants)
print("The no.of different consnants present in",word,"is:",len(word)-len(found))
