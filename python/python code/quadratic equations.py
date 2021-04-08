import math as mas
a = int(input("enter coefficients of x^2"))
b = int(input("enter coefficients of x"))
c = int(input("enter coefficient"))
d = ((b**2) - (4*a*c))
if (d>=0):
 print("roots are real")

 r1 = int(-b + mas.sqrt(d))/(2*a)
 r2 = int(-b - mas.sqrt(d))/(2*a)
 print("r1",r1) 
 print("r2",r2)
else:
 print("roots are imaginary")  

 