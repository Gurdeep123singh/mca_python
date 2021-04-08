def fibo(a,b,n,list1):
 for i in range(2,n): 
     c=a+b
     list1.append(c)
     a=b
     b=c
     fibo(a,b,n,list1)
     return list1



n = int(input("enter the no->>"))

if n==1:
    print(0)
elif n==2:
    print(0,1) 
else:
    a=0
    b=1
    fibonacci=fibo(a,b,n,list1=[])
    print(fibonacci)


