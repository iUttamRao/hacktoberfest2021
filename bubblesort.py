list1=list(input("Enter the list"))
print('List is :',list1)
n=len(list1)
temp=0
for i in range(n,-1):
    print('Hi')
    for j in range(0,i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
