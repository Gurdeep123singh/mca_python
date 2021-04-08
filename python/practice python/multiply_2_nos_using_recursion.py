''' program to multiply of two no's using recursion
it takes 2 no and check if a>b then a is add or subtract recursively and b as times to add or subtract a
if b>a then b is add or subtract recursively and a as times to add or subtract b
if both are equal simply send it as it is to fn
i/p :- a = -2 
b= 3
ans =-6
'''

def multiply(a,b,sum):               # taking 2 nos and also has sum in its parameter
    while b!=0:                      # it will run till b is not equal to 0
        if b>0:                       # if b>0 or say b is +ve
            sum+=a                     # it will add the a with b times
            x=multiply(a,b-1,sum)     # here b also decreasing its times to add the a with itself
        elif b<0:                      # if b is -ve
            sum-=a                     # then a is subracting with itsef means -ve ans
            x=multiply(a,b+1,sum)      #   and as b is -ve so for decreasing its time we have to add it with 1
        return x       
    return sum                         # returning sum


def main():                                        # defining main fn
 a = int(input("enter a first no :"))              # if 2
 b = int(input("enter a second no :"))             # if 3
 if a>b or a==b:                                    # if 2>3 or 2==2 it takes a as 3 and b as 2 times 
     multiplication=multiply(a,b,sum=0)             # and for 2==2 it takes a as a and b as b
     print(f"multiplication of two no is : {multiplication}")
 elif a<b:                                               # if 3>2 it takes a as 3 and b as 2 times
     multiplication=multiply(b,a,sum=0)  
     print(f"multiplication of two no is : {multiplication}")
 elif a==0 or b==0:                                      # if a==0 or b==0 ans is 0
     print("multiplication of two no is : 0")    
  
main()                          # calling main fn