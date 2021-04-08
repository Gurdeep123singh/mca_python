# whether a no is prime
c = int(input("enter the no "))
def prime(c):

 for i in range(2,c):
   if (c % i ==0):
     print("the no is not prime")
     break
   else:
     print("the no is prime")
     break
prime(c)