print("Enter 4 no to find greatest one :")
lis =[]
for i in range(0,4):
    print("enter",i+1,"no. :")
    a = int(input())
    lis.append(a)
print("The entered elements are :",lis) 
b = lis[0]   
for i in range(1,len(lis)):
    if b<lis[i]:
      b= lis[i]
    else:
        pass 
print("The largest element in the list is :",b)