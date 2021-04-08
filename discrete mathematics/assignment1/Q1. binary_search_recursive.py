'''
program to find no using binary search using iteration
'''

def binary(list1,no,start,end):   #  passing sorted list , no to found, start and end
 if start<=end:                    # runs till end is greater than or equal to start
     mid=(start+end)//2
     if no>list1[mid]:                              # if no is greater than mid means start=mid+1
         return binary(list1,no,mid+1,end)
     elif no<list1[mid]:                            # if no is lesser than mid means end=mid-1
         return  binary(list1,no,start,mid-1)
     elif no==list1[mid]:
         return mid                                   # if no= mid
 else:
     return -1           

number = int(input("how many no you want to take"))
list1=[]
print("enter elements:")
for i in range(0,number):
    c=int(input())
    list1.append(c)
print("the elements you give is:",list1)

for i in range(number):                                   # sort in ascending order
    for j in range(number):
     if list1[i]<list1[j]:
         c=list1[i]
         list1[i]=list1[j]
         list1[j]=c
    else:
         pass
print("sorted list",list1)    


no = int(input("enter the no which u want to find->>"))
index=binary(list1,no,start=0,end=len(list1)-1)
if index == -1:
    print("no not found") 
else:
    print(f"the {no} is at {index}")

