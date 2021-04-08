## hamdard(element wise multiplication)
p = int(input("enter no of rows :"))            # taking no of rows
q = int(input("enter no of columns :"))         # taking no of col
matrixA=[]
print("enter elements for matrix A :")

# taking elements in the matrixA by row wise
for i in range(p):
    a=[]                 # row wise
    for j in range(q):
        print(f"enter element for{i} th row {j}th column:")
        c=int(input())
        a.append(c)
    matrixA.append(a)

# printing matrix A   
print(f"the {p} X {q} matrixA is :")
for i in range(p):
    for j in range(q): 
     print(matrixA[i][j]," ",end="")
    print() 

# taking elements in the matrixB by row wise
matrixB=[]
print("enter elements for matrix B :")

for i in range(p):
    b=[]
    for j in range(q):
        print(f"enter element for{i} th row {j}th column:")
        d=int(input())
        b.append(d)
    matrixB.append(b)

 # printing matrixB
    
print(f"the {p} X {q} matrixB is :")
for i in range(p):
    for j in range(q): 
     print(matrixB[i][j]," ",end="")
    print()   

# doing multipliction element wise and appended in the new_matrix    
new_matrix=[]
for i in range(p):
    l=[]
    for j in range(q):
        multiply = matrixA[i][j] * matrixB[i][j]
        l.append(multiply)
    new_matrix.append(l)


#  printing new_matrix
print(f"the {p} X {q} new matrix is :")
for i in range(p):
    for j in range(q): 
     print(new_matrix[i][j]," ",end="")
    print()     

