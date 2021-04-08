# program to find sum of diagonal

p = int(input("enter no of rows or columns as rows and columns are same"))
matrix=[]

# taking elements row wise in matrix 
for i in range(p):
    a=[]
    for j in range(p):
        print(f"enter element for{i} th row {j}th column:")
        c=int(input())
        a.append(c)     # appending elements   
    matrix.append(a)    

# printing matrix    
print(f"the square {p} X {p} matrix is :")
for i in range(p):
    for j in range(p): 
     print(matrix[i][j]," ",end="")
    print() 

## sum of diagonal
primary_sum=0
secondary_sum=0
for i in range(p):
    for j in range(p):
        if i==j:
            primary_sum += matrix[i][j]   # for primary diagonal
    secondary_sum += matrix[i][p-(i+1)]   # for secondary diagonal

print("primary diagonal sum is :",primary_sum)   
print("secondary diagonal sum is :",secondary_sum)     

