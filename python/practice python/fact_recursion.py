'''
program to find factorial from 1 to given no and from n to 1 using recursion
used only 2 functions and returning list of factorials .
in one fn printing of reverse factorial and calling is there and in other defining function and printing of 
1 to n factorial is there.. 
 i/p -> 6

 o/p->

 1 ! is : 1
 2 ! is : 2
 3 ! is : 6
 4 ! is : 24
 5 ! is : 120
 6 ! is : 720

reverse order of factorial is :
 6 ! is : 720
5 ! is : 120
4 ! is : 24
3 ! is : 6
2 ! is : 2
1 ! is : 1

'''
def main():
 number= int(input("enter number:"))   # taking number
        
 if(number>0):
     print(f"factorial from 1 to {number} is->>>\n")
 fact(number)                        # calling

 
 # for printing factorials 
 if(number>0):
  # factorial in reverse order
     print(f"\nthe factorial from {number} to 1 is ->>>\n")
     for i in range(len(c)-1,-1,-1):  # going from length to 0  or say it is in decreasing order 
         print(f"factorial of { i+1 } is : {c[i]}")
 else:
     print(f"{number} ! is :",1)
 
 
c=[]  #  global list

def fact(n):
 
 if(n>0):                    # if >0
     a=n*fact(n-1)              # storing factorial 
     c.append(a)                 # appending factorials in the list
     print(n," ! is:",a)         # printing factorials upto given no from 1 to number
     return a                     # returning value
        
 else:          # if 0                  
     return 1





main()


