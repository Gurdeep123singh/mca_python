'''
program to find factorial from 1 to given no and from n to 1 using  without recursion
used only 2 function and without returning

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
 n= int(input("enter no upto which you want factorial :\n"))  # taking input
 a=1
 list1=[]
 if (n>0):      # if greater than 0 it prints this statement
     print(f"\nfactorial from 1 to {n} is :\n")
 factorial(n,a,list1)    

def factorial(n,a,list1):
 if(n==0):                                 # if 0 then prints factorial of 0
     print("factorial of 0 is:",a)
 else:    
     for i in range(1,n+1):                    # if greater than 0
         a=a*i                                 # its doing factorial
         list1.append(a)                       # appending factorial in the list
         print(f"factorial of {i} is : {a}")   
 if (n>0):                                      # executes when n is greater than 0
     print("\nreverse order of factorial is ->>> ")   
     print(f"\nfactorial from {n} to 1 is :\n")
     for i in range(len(list1)-1,-1,-1):            # going from length to 0  or say it is in decreasing order 
         print(f"factorial of { i+1 } is : {list1[i]}")    # printing in reverse order

main()     
    