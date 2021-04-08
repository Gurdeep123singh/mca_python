print("enter 1 for true1 and 0 for false :")
p=[]
q=[]

print("enter size for p and which is same for all variables:")
size=int(input("enter size :"))

print("enter 1 or 0 for p:")
for i in range(size):
 c=int(input())
 print(bool(c))
 p.append(bool(c))
print(p)

print("enter 1 or 0 for q:")
for i in range(size):
 d=int(input())
 print(bool(d))
 q.append(bool(d))
print(q)

print("\t\t\t 1.)  MODUS PONUS  2.)  MODUS TOLLENS")
while True:
 print("1.)  MODUS PONUS  2.)  MODUS TOLLENS  OR EXIT(0)")    
 option=int(input("enter option:"))   
 if option==1:   
     print("\t\t\t\t\t------------------------------\n")
     print("\t\t\t\t\t1.)   modus ponus ")
     print("\t\t\t\t\t------------------------------\n\n")
     print(f"\t\t\t\t\t (~p or  q) ^ p     ")
     print("\t\t\t\t\t------------------------------\n")
     print(" ~p is :\n")
     for i in range(len(p)):
         print("\t\t\t\t\t~",p[i],"                           |",   (not(p[i])))
     print(" q is :\n")    
     for i in range(len(p)):
         print("\t\t\t\t\t",q[i])
     print("\n")  
     print(f"\t\t\t\t\t (~p or  q) ^ p  ")
     print("\t\t\t\t\t------------------------------\n")  
     for i in range(len(p)):
         print("\t\t\t\t\t(",q[i],"or ", (not(p[i])),")and ", p[i],"                           |",   ((q[i] or (not(p[i]))) and p[i]))

 elif option==2:
     print("\t\t\t\t\t------------------------------\n")
     print("\t\t\t\t\t2.)   modus tollens ")
     print("\t\t\t\t\t------------------------------\n\n")
     print(f"\t\t\t\t\t (~p or  q) ^ ~q     ")
     print("\t\t\t\t\t------------------------------\n")
     print(" ~p is :\n")
     for i in range(len(p)):
         print("\t\t\t\t\t~",p[i],"                              |",   (not(p[i])))
     print(" q is :\n")    
     for i in range(len(p)):
         print("\t\t\t\t\t",q[i])
     print("\n")  
     print(" ~q is :\n")    
     for i in range(len(p)):
         print("\t\t\t\t\t~",q[i],"                               |",    (not(q[i])))
     print("\n")  
     print(f"\t\t\t\t\t (~p or  q) ^ ~q  ")
     print("\t\t\t\t\t------------------------------\n")  
     for i in range(len(p)):
         print("\t\t\t\t\t(",q[i],"or ", (not(p[i])),")and ", (not q[i]),"                            |",    ((q[i] or (not(p[i]))) and (not q[i])))

 elif option==0:
     exit()   