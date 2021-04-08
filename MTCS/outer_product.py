# program to find outer product
# by taking n*1 and 1*m matrix 
# and making n*m matrix

row = int(input("enter no of rows for matrix 1: "))
col =  int(input("enter no of columns for matrix 2: "))

# making matrix1 by taking elements row wise 
matrix1=[]
print("give the elements for matrix1 :")
for i in range(row):
  l1=[]
  for j in range(0,1):
   print(f"the element of{i} th row of 1 th column is : ")
   c= int(input())
   l1.append(c)
  matrix1.append(l1) 

# printing matrix1
print(f"the matrix1 of {row} X 1 is: ")
for i in range(row):
    for j in range(0,1):
      print(matrix1[i][j]," ")  

# taking elements in matrix2 
matrix2=[]
print("give the elements for matrix2 :")
for i in range(0,1):
 l2=[]
 for j in range(col):
    print(f"the element of 1 th row of {col} th coumn is : ")
    c= int(input())
    l2.append(c)
 matrix2.append(l2)     

## printing matrix2 of 1xn

print(f"the matrix2 of 1 X {col} is: ")
for i in range(0,1):
  for j in range(col):
    print(matrix2[i][j]," ",end="")
  print()  

# doing outer product and making new matrix of row*col
new_matrix=[]
for i in range(row):
  l3=[]
  for j in range(col):
    c=matrix1[i][0]*matrix2[0][j]
    l3.append(c)
  new_matrix.append(l3) 

# printing new matrix of n*m or row*col
print(f"the new matrix of {row} X {col} is: \n")
for i in range(row):
  for j in range(col):
    print(new_matrix[i][j]," ",end="")
  print()  



    

     