# program to do matrix multiplication
# taking two matrix  p*n  n*q  where n is same for both matrix

p = int(input("enter no of rows for matrix1"))  # p*n  n*q
q= int(input("enter no of columns for matrix2"))
n= int(input("enter no of column for matrix1 / row for matrix2"))

# taking elements row wise for matrix1
print("enter the elements for matrix1 :")
matrixA=[]
for i in range(p):
    a=[]
    for j in range(n):
        print("give element",j+1,"for",i,"th row") 
        a.append(int(input()))
    matrixA.append(a)   # taking entries row wise

# printing matrix1    
print("MatrixA of ", p ,"X" ,n, "is: ")

for i in range(p):
    for j in range(n):
        print(matrixA[i][j]," ",end="")
    print()    

# taking elements row wise for matrix2        
print("enter the elements for matrix2 :")
matrixB=[]
for i in range(n):
    b=[]
    for j in range(q):
        print("give element",j+1,"for",i,"th row") 
        b.append(int(input()))
    matrixB.append(b)   # taking entries row wise

# printing matrix2    
print("MatrixB of ", n ,"X" ,q, "is: ")

for i in range(n):
    for j in range(q):
        print(matrixB[i][j]," ",end="")
    print()          

# taking matrix of value 0 in order of p*q              
r=[[0 for i in range(q)] for j in range(p)]


# doing multiplication
for i in range(p):
        for j in range(q):
            for k in range(n):
                r[i][j] =r[i][j] + (matrixA[i][k] * matrixB[k][j])



# printing new matrix                
print("New matrix after matrix multiplication of ",p, "X",q, " is : ")  

for i in range(p):
    for j in range(q):
        print(r[i][j],"  ",end="")
    print()    
           
           

