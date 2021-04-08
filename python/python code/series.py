from math import *  # importing maths 
# cos series and exponential series 

def main():
    n = int(input("sum of n terms of series: ")) # taking n terms
    x = int(input("enter x :"))   # taking x value
    
    print("sum of series 1", s1(n,x))  # for cos
    print("sum of series 2", s2(n,x))  # for exp

def fact(n):  # doing factorial
   if(n==0):
       return 1  # if 0 return 1 where fact(n) calls
   else:
       return(n*fact(n-1))  # doing recursive factorial eg 1*1 , 2*1*1 , 3*2*1*1*1 etc

# 1 -(x^2)/2! + (x^4)/4! ........ (x^n)/n!

def s1(n,x):  # taking values from main
    sum=1
    if(n==1):   # if 1 then sum=1
        return sum
    for i in range(n):   # going to n terms
        sum=sum+(pow(-1,i))*((pow(x,2*i))/fact(2*i)) # 1+ (-1)^i*x^2*i / factorial (multiple of 2)
    return sum  # returning sum value

# e^x =1+ (x)/1! + (x^2)/2! + (x^3)/3!.......

def s2(n,x):   # taking values from main
    sum=1
    if (n==1):   # if 1 then sum=1
        return sum
    for i in range(n):   # going to n terms
        sum = sum +pow(x,i)/fact(i)   # 1+x^i/factorial (i)
    return sum

main() # calling main