# *
# **
# ***
# ****
n = int(input("enter the no of rows"))  # input
for i in range(1,n+1):  # from 1 to row+1
  for j in range(1,i+1): # from 1 to 2, 1 to 3, 1to 4 etc print * in col
    print("*",end="") # end is used for making in one line with space
  print() # for  outer loop # for new line
