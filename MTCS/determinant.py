#Program to find out Determinant of matrix having 3 functions 


from copy import deepcopy  # using deepcopy  by this it doesn't affect the original matrix
def main():
   
    n=int(input("Enter the order of the matrix: \n"))   # taking order of matrix

    
    print("\nEnter the elements of the matrix one by one: \n")
    A=[[int(input()) for i in range (n)] for j in range (n)]  # taking elements one by one 

    # print the matrix

    print('Matrix is:')
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j],end=" ")
        print()

    # print the determinant of matrix

    result = det(A)
    print('Determinant: ',result)


def det(A):  # for dterminant
    row=len(A) 
    determinant=0
    
    if(row == 2):                                              # for matrix order 2
        determinant = (A[0][0]*A[1][1])-(A[1][0]*A[0][1])
        return determinant
    else:
        
     # taking cofactor for above order of 2
        for i in range(row):            
            cofactor=((-1) ** i) * A[0][i] * det(smallerMatrix(A,0,i))   
            determinant +=cofactor
        return determinant                                                  #return determinate 



def smallerMatrix(matrix,row,column):     # used for deletion of row and column 
    
    newMatrix=deepcopy(matrix)
    newMatrix.remove(matrix[row])
    for i in range(len(newMatrix)):
        newMatrix[i].remove(newMatrix[i][column])
    return newMatrix 


main()
