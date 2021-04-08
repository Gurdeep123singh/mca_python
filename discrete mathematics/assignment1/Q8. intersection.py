'''
program to make intersection of 2 sets
first i make setA and setB as list then later i have made it set object as set doesnt has duplicate items
'''
set1_size= int(input("enter size of 1st set:"))     
set2_size= int(input("enter size of 2nd set:"))
setA=[]                                              # making setA as list
setB=[]                                               # making setA as list
print("enter elements for setA:")
for i in range(set1_size):                           # appending elements  for setA
    setA.append(input())
print("enter elements for setB:")                     
for i in range(set2_size):                            # appending elements  for setB
    setB.append(input())    
print("setA is :",set(setA))                       # printing setA as set
print("setB is :",set(setB))                       # printing setB as set
intersection=[]                                     # intersection list

if set1_size > set2_size or set1_size==set2_size:                # if set1 size is greater than or equal to size of set2
     for i in range(set2_size):                             # then using setB and appending elements of setB in intersection
            
         if setB[i] in setA:                        # checking if setB elements are in setA
             intersection.append(setB[i])           # if there means intersection is there
         else:
             pass                                     # else pass
     print("intersection of A and B :",set(intersection)   )    
else:
    for i in range(set1_size):                                 # if set1 size is lesser than or not equal to size of set2
        
        if setA[i] in setB:                           # then using setA and appending elements of setA in intersection
            intersection.append(setA[i])              # checking if setA elements are in setB # if there means intersection is there
        else:
            pass                                       # else pass
    print("intersection of A and B :",set(intersection))