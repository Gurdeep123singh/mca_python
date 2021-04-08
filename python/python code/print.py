# it has all the patterns 
# it takes input and doesnt return but only prints the pattern 

# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5

a = int(input("enter no. of rows"))  # takes input
for i in range(1,a+1):  # 1 to rows+1
 for j in range(1,i+1):   # 1 to 2, 1 to 3, 1 to 4
   print(j, end = "")     # prints 1 , 1 2 , 1 2 3 , 1 2 3 4  # end used for making in 1 line 
 print()   # used for print another rows

#  1
#  2 2
#  3 3 3
#  4 4 4 4

a = int(input("enter no. of rows"))
for i in range(1,a+1):  # 1 to rows+1
 for j in range(1,i+1):  # 1 to 1 , 1 to 2 , 1 to 3
   print(i, end = "")    # prints rows values in col 
 print()   # used for printing another rows

# 3 2 1
# 2 1 
# 1

a = int(input("enter no. of rows"))
for i in range(a,0,-1):  # row to 0 and -1 used for decrementing
 for j in range(i,0,-1):  # going row length  to 0 and -1 for decrementing
   print(j, end = "")  # printing row length to 0 i.e 3 2 1 , 2 1, 1
 print()   # used for printing another rows

# 4 4 4 4
# 3 3 3 
# 2 2 
# 1

a = int(input("enter no. of rows"))
for i in range(a,0,-1): # length of row to 0 
 for j in range(i,0,-1): # length of row to 0 
   print(i, end = "")   # prints row value in all col till 0 and starts from length of row
 print()  # used for printing another rows

    #          1
    #       2  1   2
    #    3  2  1   2  3
    # 4  3  2  1   2  3  4   


a = int(input("enter no. of rows"))
for i in range(1,a+1):
 for j in range(1,a-i+1):  
     print(end=" ")   # for spacing  
 for j in range(i,0,-1):
  print(j,end="")   # col val is printed in col (row i.e. last value to 0 i.e start)
 for j in range(2,i+1) :
   print(j,end="")   # started from 2 to i+1
 print()   # for printing another rows

########
########
########
########

a = int(input("enter no. of rows"))
for i in range(1,a+1):    # 1 to row+1    
 for j in range(a+1,0,-1):  # row+1 to start and -1 used for decrementing
   print("#",end="")   # is printed
 print()

# 1234
#  234
#   34
#    4

a = int(input("enter no. of rows"))
for i in range(1,a+1):
   
 for j in range(1,i+1): # for making spaces
     print(" ", end="")   # first spacing
 for j in range(i,a+1):  # 1 to row+1
   print(j,end="")      # j value is printed   
 print()  # for printing another row

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

s = int(input("enter no of rows"))
for i in range(1,s+1): # for 1 to row+1
 for j in range(s-i+1,0,-1): # -1 for decresing
   print( j, end = "") # printing row+1 - rows ranges 
 print() # print another rows

# *******
# ******
# *****
# ****
# ***
# **
# *

s = int(input("enter no of rows")) 
for i in range(1,s+1):                # for 1 to row+1
 for j in range(s-i+1,0,-1): # -1 for decresing
   print("*", end = "")    # printing stars
 print()                    # print another rows


# *****
# *   *
# *   *
# *   *
# *****

row = int(input("enter no of rows"))

for i in range(row):
  for j in range(row):
    if i==0 or i==row-1  or j==0 or j==row-1 :   # print stars values in that col where (row =0, row-1),(col=0,
      print("*",end ="")                         # and in last col)
    else:                                 
      # prints space where above conditions doesnt exists
      print(" ",end="")
  print()    # printing another rows

#  $$$$$
#   $$$$
#    $$$
#     $$
#      $

a = int(input("enter no. of rows"))
for i in range(1,a+1):
   
 for j in range(1,i+1): # for making spaces
     print(" ", end="") # first making spaces so used first spacing col
 for j in range(i,a+1):
   print("$",end="")      # now printing $  
 print()

#       $
#      $$
#     $$$
#    $$$$
#   $$$$$
#  $$$$$$    

a = int(input("enter no. of rows"))
for i in range(1,a+1):
   
  for j in range(a-i,0,-1): # for making spaces 
    print(" ", end="") # first making spaces
  for j in range(a,a-i,-1): # row length  to length (row) -i (ranges) end to start
    print("$", end="")       
  print() 

#    $
#   $$$
#  $$$$$
# $$$$$$$             
         

# Divide this into 3 parts
a = int(input("enter no. of rows"))
for i in range(1,a+1):      # for 1 to row+1
   
  for j in range(a-i,0,-1): # for making spaces
    print(" ", end="") # 1 spacing
  for j in range(a,a-i,-1):
    print("#", end="")     # print # from  row value to startvalue
  for j in range(a+1,a+i): # row+1 to row+i(ranges)
    print("#",end="")    
  print()   # print another rows

   #
  ###
 #####
#######
 #####
  ###
   #  


a = int(input("enter no. of rows"))                          ## for upper pyramid
for i in range(1,a+1):                # for 1 to row+1
   
  for j in range(a-i,0,-1): # for making spaces
    print(" ", end="") 
  for j in range(a,a-i,-1):
    print("#", end="")     # print # from  row value to startvalue
  for j in range(a+1,a+i):   # row+1 to row+i(ranges)
    print("#",end="")
  
  print()    # print another rows
                                                                ## for lower pyramid
for i in range(a-1,0,-1): # for reversing  last row to start row
  for j in range(a-i,0,-1): # for making spaces
    print(" ", end="")   # end is used to go in same line
  for j in range(a,a-i,-1):
    print("#", end="")       # print # from  row value to startvalue
  for j in range(a+1,a+i):    # row+1 to row+i(ranges)
    print("#",end="")
  
  print()              # printing another rows

# $$$$$$$$
#  $$$$$$
#   $$$
#    $    

                                                          ## for lower pyramid
for i in range(a-1,0,-1): # for reversing
  for j in range(a-i,0,-1): # for making spaces
    print(" ", end="") # end is used to go in same line
  for j in range(a,a-i,-1):
    print("#", end="")     # print # from  row value to startvalue
  for j in range(a+1,a+i):  # row+1 to row+i(ranges)
    print("#",end="")
  
  print()              # printing another rows

#       *
#     *   *
#    *     *
#   *       *
#  ***********          


a = int(input("enter no. of rows"))
for i in range(1,a+1):                   # from 1 to row+1
   
  for j in range(1,(a*2)): 
    if i==a or (i+j)==a+1 or (j-i)==a-1 :  # print stars where i= last row , row +col = len(row)+1 and 
     print("*", end="")                    #  col - row = len(row)-1
    else:
      print(" ",end="")                     # otherwise prints spacing
  
  print()                                    # prints another rows

#     *
#    * *
#   *   *
#  *     *
# * * * * *


a = int(input("enter no. of rows"))
k=2
for i in range(1,a+1):
   
  for j in range(1,(a*2)):  # 1 to 2*row
    if (i+j)==a+1 or (j-i)==a-1: # for row+col = 5 and row-col=3
     print("*", end="") 
    elif i==a and j!=k:  # for last row and having even col no star is there
      print("*",end="")
      k=k+2   # incrementing k for even nos
    else:
      print(" ",end="")
  
  print()   # printing another rows

# * * * * *
#  *     *
#   *   *
#    * *
#     *

a = int(input("enter no. of rows"))
k=2
for i in range(a+1,0,-1):   # from row value +1 to 0 and -1 for decrementing
   
  for j in range(1,(a*2)): 
    if (i+j)==a+1 or (j-i)==a-1: # for row+col = 5 and row-col=3
     print("*", end="") 
    elif i==a and j!=k:  # for last row and having even col no star is there
      print("*",end="")
      k=k+2   # incrementing k for even nos
    else:
      print(" ",end="")  # for spacing
  
  print()           # print another rowsS

#     *
#    * *
#   *   *
#  *     *
# *       *
# *       *
#  *     *
#   *   *
#    * *
#     *


a = int(input("enter no. of rows"))
### upper triangle

for i in range(1,a+1):  # here no step as step is decreasing by default step is +1.
   
  for j in range(1,(a*2)): # 1 to 2*row
    if (i+j)==a+1 or (j-i)==a-1: # for row+col = 5 and row-col=3
     print("*", end="") # print stars if above condition
    
    else:
      print(" ",end="") # prints otherwise space
  
  print() # prints another rows

## lower triangle
for i in range(a,0,-1):  # -1 for decreasing  # row value to 0 i.e  last to 0
   
  for j in range(1,(a*2)):   # 1 to 2*row
    if (i+j)==a+1 or (j-i)==a-1: # for row+col = 5 and row-col=3
     print("*", end="")    # print stars
                           
    else:
      print(" ",end="")  # otherwise print stars
  
  print() # print another rows


# *
# **
# ***
# ****
n = int(input("enter the no of rows"))  # input
for i in range(1,n+1):  # from 1 to row+1
  for j in range(1,i+1): # from 1 to 2, 1 to 3, 1to 4 etc print * in col
    print("*",end="") # end is used for making in one line with space
  print() # for  outer loop # for new line
