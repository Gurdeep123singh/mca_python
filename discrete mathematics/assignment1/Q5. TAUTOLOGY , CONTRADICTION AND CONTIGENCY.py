'''
program for 1.)  TAUTOLOGY 2.)  CONTRADICTION  3.)  CONTIGENCY 
'''
print("enter 1 for true and 0 for  false :")
p=[]
q=[]

print("enter size for p and which is same for all variables:")
size=int(input("enter size: "))

print("enter 1 or 0 for p:")
for i in range(size):
 c=int(input())
 print(bool(c))
 p.append(bool(c))
print(p)

print(" \t\t\t1.)  TAUTOLOGY 2.)  CONTRADICTION  3.)  CONTIGENCY  ")
while True:
    print("0  FOR EXIT  1  TAUTOLOGY 2  CONTRADICTION  3  CONTIGENCY  ")
    option=int(input("enter choice  FROM ABOVE STATEMENT:"))
    if option==1:
        
     print("\t\t\t\t\t------------------------------\n")
     print("\t\t\t\t\t1.)   TAUTOLOGY ")
     print("\t\t\t\t\t------------------------------\n\n")
     print(f"\t\t\t\t\t p or(~p)     ")
     print("\t\t\t\t\t------------------------------\n")
     print(" ~p is :\n")
     for i in range(len(p)):
         print("\t\t\t\t\t~",p[i],"                           |", (not(p[i])))
     print("\n")
     print("  p is :\n")    
     for i in range(len(p)):
         print("\t\t\t\t\t",p[i])
     print("\n")
     print(f"\t\t\t\t\t p or(~p)     ")
     print("\t\t\t\t\t------------------------------\n")

     for i in range(len(p)):
         print("\t\t\t\t\t(",p[i],"or ", (not(p[i])),")                          |", (p[i] or (not(p[i]))))
    
    elif option==2:
        
     print("\t\t\t\t\t------------------------------\n")
     print("\t\t\t\t\t2.)   CONTRADICTION ")
     print("\t\t\t\t\t------------------------------\n\n")
     print(f"\t\t\t\t\t p and(~p)     ")
     print("\t\t\t\t\t------------------------------\n")
     print(" ~p is :\n")
     for i in range(len(p)):
         print("\t\t\t\t\t~",p[i],"                           |", (not(p[i])))
     print(" p is :\n")    
     for i in range(len(p)):
         print("\t\t\t\t\t",p[i])
     print("\n")  
     print(f"\t\t\t\t\t p and(~p)     ")
     print("\t\t\t\t\t------------------------------\n")  
     for i in range(len(p)):
         print("\t\t\t\t\t(",p[i],"and ", (not(p[i]))," )                         |",  (p[i] and (not(p[i]))))
    
    elif option==3:
     print("enter 1 or 0 for q:")
     for i in range(size):
         d=int(input())
         print(bool(d))
         q.append(bool(d))
     print("the boolean you choose for q is:",q)   
     print("\t\t\t\t\t------------------------------\n")
     print("\t\t\t\t\t3.)   CONTIGENCY ")
     print("\t\t\t\t\t------------------------------\n\n")
     print(f"\t\t\t\t\t p OR q     ")
     print("\t\t\t\t\t------------------------------\n")
     print(" p is :\n")
     for i in range(len(p)):
         print("\t\t\t\t\t",p[i] )
     print(" q is :\n")    
     for i in range(len(p)):
         print("\t\t\t\t\t",q[i] )
     print(f"\t\t\t\t\t  p \tor     q is :: \n") 
     print("\t\t\t\t\t------------------------------\n")   
     for i in range(len(p)):
         print("\t\t\t\t\t",p[i],"\tor\t",q[i],"                              |",  (p[i] or q[i]))    
    
    elif option==0 :
        exit()
