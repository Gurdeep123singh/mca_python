'''
program to make union of 2 sets
first i make setA and setB as list then later i have made it set object as set doesnt has duplicate items
'''

set1_size= int(input("enter size of 1st set:"))     
set2_size= int(input("enter size of 2nd set:"))
setA=[]                                                   # making setA as list
setB=[]                                                   # making setb as list
print("enter elements for setA:")
for i in range(set1_size):                                # appending elements  for setA
    setA.append(input())
print("enter elements for setB:")    
for i in range(set2_size):                                # appending elements  for setB
    setB.append(input()) 

print("setA is :",set(setA))                             # printing setA as set object
print("setB is :",set(setB))                             # printing setB as set object

union=[]
if set1_size > set2_size or set1_size==set2_size:            # if set1 size is greater than or equal to size of set2
     union=setA                                            # then using setA in union 
     for i in range(set2_size):
        
         if setB[i] in setA:                              # if elements of setB in setA then pass
             pass
         else:                                                #  appending elements of setB in union
             union.append(setB[i])
     print("union of A and B :",set(union))            
else:
    union=setB
    for i in range(set1_size):                         # if set1 size is lesser than or not equal to size of set2
        
        if setA[i] in setB:              # then checking if setA elements in setB , if there, not append
            pass
        else:                                        # else appends
            union.append(setA[i]) 
    print("union of A and B :",set(union))                    # making union as set object