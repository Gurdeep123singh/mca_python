n= int(input("enter no upto which you want row :"))
for i in range(0,n):
  for j in range(n-i-1,0,-1):
     print(" ",end="")
  for j in range(n,n-i,-1):
     print("*",end="")
  for j in range(n+1,n+i):
     print("*",end="")
  print()            

# or
n= int(input("enter no upto which you want row :"))
for i in range(n):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-i-1))

n= int(input("enter no upto which you want row :"))
for i in range(0,n):
    for j in range(0,i+1):    # for i in range(n)     
     print("*",end="")        #    print("*" *(i+1))
    print()        

n= int(input("enter no upto which you want row :"))
for i in range(n):
    for j in range(n):
     if i==0 or i==n-1 or j==0 or j==n-1:
         print("*",end="")
     else: 
         print(" ", end="")    
    print()



