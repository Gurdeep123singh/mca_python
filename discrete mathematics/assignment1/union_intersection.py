'''
program to make union and intersection by taking two sets from user and then checking union and intersection
'''
set1_size= int(input("enter size of 1st set:"))     
set2_size= int(input("enter size of 2nd set:"))
setA=[]
setB=[]
print("enter elements for setA:")
for i in range(set1_size):
    setA.append(input())
print("enter elements for setB:")    
for i in range(set2_size):
    setB.append(input())    
print("setA is :",setA)
print("setB is :",setB)
intersection=[]
union=[]
print("what you want to do ::")
print("Union(a) or Intersection(b) or exit(e)")
option=input("enter a or b :")


if option=='a':
 if set1_size > set2_size or set1_size==set2_size:
     union=setA
     for i in range(set2_size):
        
         if setB[i] in setA:
             pass
         else:
             union.append(setB[i])
     print("union of A and B :",union)            
 else:
     union=setB
     for i in range(set1_size):
        
         if setA[i] in setB:
             pass
         else:
             union.append(setA[i]) 
     print("union of A and B :",union)          

elif option=='b':
 if set1_size > set2_size or set1_size==set2_size:
     for i in range(set2_size):
        
         if setB[i] in setA:
             intersection.append(setB[i])
         else:
             pass
     print("intersection of A and B :",intersection)       
 else:
     for i in range(set1_size):
        
         if setA[i] in setB:
             intersection.append(setA[i])
         else:
             pass 
     print("intersection of A and B :",intersection)                            
else:
    exit()