'''
program to find no using binary search using iteration
'''
number = int(input("how many no you want to take"))
list1=[]
print("enter elements:")                             #  taking elements in list
for i in range(0,number):
    c=int(input())
    list1.append(c)
print("the elements you give is:",list1)

for i in range(number):                                  # sorted in ascending order
    for j in range(number):                         
     if list1[i]<list1[j]:                                
         c=list1[i]
         list1[i]=list1[j]
         list1[j]=c
    else:
         pass
print("sorted list",list1)  

def binary(list1,no):                             # passing sorted list and no which we have to search
    start=0
    end=len(list1)-1                             # end= length-1
    while start<=end:                              # run till length of start is under or equal to end length
        mid=(start+end)//2                      # mid value
        if no==list1[mid]:                    # if no is in mid of list
            return mid                          
        elif no > list1[mid]:                   # if no is greater than mid
            start=mid+1                         # then start index = mid+1
        elif no < list1[mid]:                  # if no is lesser than mid
            end=mid-1                         # then end index = mid-1
    return -1                                 # if not found then index -1



no = int(input("enter the no which u want to find->>"))
index=binary(list1,no)
if index == -1:                     
    print("no not found") 
else:
    print(f"the {no} is at {index}")


        


