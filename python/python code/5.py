a = int(input("enter the no"))
print(a)
b = int(input("enter the no"))
print(b)
c = int(input("enter the no"))
print(c)

compare(a,b,c)


def compare(a,b,c):
   
 if (a>b and a>c):
   print(a,"a is greatest")

 elif (b>c and b>a):
   print(b,"b is greatest")
        
 elif (c>a and c>b):
   print(c,"c is greatest")
 else:
   print(a,b,c ,"are equal")   

