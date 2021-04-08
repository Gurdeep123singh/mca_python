# program to find max and min from a vector


# taking elements in the list
number = int(input("enter number of terms you want in the vector"))
list1=[]
print("enter elements in a list: ")
for i in range(number):
 c=int(input())
 list1.append(c)
print("the elements are :",list1)


largest=list1[0]      # taking element 1st from the list

# checking for maximum
for i in range(1,len(list1)):
     if largest<list1[i]:          # comparing 1st element from other elements
         largest=list1[i]         
     else:
         pass    
print("the maximum no in the vector is : ",largest)    


# checking for minimum
smallest=list1[0]
for i in range(1,len(list1)):
     if smallest<list1[i]:
         pass
     else:
         smallest=list1[i] 
print("the minimum no in the vector is : ",smallest)             