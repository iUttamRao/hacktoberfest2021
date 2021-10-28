line=input("Enter a Line")
lowercount=uppercount=0
digitcount=alphacount=0
for i in line:
    if i.isalpha():
        alphacount+=1
    elif i.islower():
        lowercount+=1
    elif i.isupper():
        uppercount+=1
    if i.isdigit():
        digitcount+=1

print("Number of alphabet is :",alphacount)
print("Number of upper letter :",uppercount)
print("Number of digit : ",digitcount)
print("Number of lower lrtter :",lowercount)
