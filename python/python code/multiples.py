def main():
 row1= int(input("Input number of rows: "))
 print(multiple(row1))   # calling multiple function

def multiple(row1):
 mlist = [[row1 for col in range(5)] for row in range(row1)]  # making matrix 

 for row in range(row1):
     for col in range(5): # col is fixed as there is multiple of 5 
         mlist[row][col]= (row+1)*(col+1) # multiplying row and col
 return mlist       # returning mlist 
main()        # calling main function