'''
program for 1.) IDENTITY LAW  2.) IMPODENT LAW  3.) DOMINATION  4.) DOUBLE NEGATION  5.) ASSOCIATIVITY LAW  6.) DEMORGANS LAW 
'''
print("enter 1 for true and 0 for false :")
p=[]
q=[]
r=[]
print("enter size for p and which is same for all laws:")
size=int(input("enter size: "))

print("enter 1 or 0 for p:")
for i in range(size):
 c=int(input())
 print(bool(c))
 p.append(bool(c))
print(p)

print("\t\t\t 1.) IDENTITY LAW  2.) IMPODENT LAW  3.) DOMINATION  4.) DOUBLE NEGATION  5.) ASSOCIATIVITY LAW  6.) DEMORGANS LAW \n")
while True:
  print("  1 IDENTITY LAW  2 IMPODENT LAW  3 DOMINATION  4 DOUBLE NEGATION  5 ASSOCIATIVITY LAW  6 DEMORGANS LAW OR EXIT(0)")
  choice=int(input("enter choice FROM ABOVE POINTS:"))
  if choice==1:
    print("\t\t\t\t\t------------------------------\n")
    print("\t\t\t\t\t1.)    IDENTITY LAW ")
    print("\t\t\t\t\t------------------------------\n\n")
    print(f"\t\t\t\t\tp \t^ \tTrue     ")
    print("\t\t\t\t\t------------------------------\n")
    for i in range(len(p)):
      print(f"\t\t\t\t\t{p[i]} \t^ \tTrue         |{p[i] and True}")
   
    print(f"\n\t\t\t\t\tp \tor \tFalse   ")
    print("\t\t\t\t\t------------------------------\n")
    for i in range(len(p)):
     print(f"\t\t\t\t\t{p[i]} \tor \tFalse         |{p[i] or False}")  

  elif choice==2:
   print("\t\t\t\t\t------------------------------\n")
   print("\t\t\t\t\t2.)   IDEMPOTENT LAW ")
   print("\t\t\t\t\t------------------------------\n\n")
   print(f"\t\t\t\t\tp \tor \tp     ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print(f"\t\t\t\t\t{p[i]} \t^ \tTrue           |{p[i] or p[i]}")
   
   print(f"\n\t\t\t\t\tp \t^ \tp   ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print(f"\t\t\t\t\t{p[i]} \tor \tFalse           |{p[i] and p[i]}") 

  elif choice==3:
   print("\t\t\t\t\t------------------------------\n")
   print("\t\t\t\t\t3.)   DOMINATION LAW ")
   print("\t\t\t\t\t------------------------------\n\n")
   print(f"\t\t\t\t\tp \t^ \tFalse     ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print(f"\t\t\t\t\t{p[i]} \t^ \tFalse          |{p[i] and False}")
   
   print(f"\n\t\t\t\t\tp \tor \tTrue   ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print(f"\t\t\t\t\t{p[i]} \tor \tTrue             |{p[i] or True}")

  elif choice==4:
   print("\t\t\t\t\t------------------------------\n")
   print("\t\t\t\t\t4.)   DOUBLE NEGATION  LAW ")
   print("\t\t\t\t\t------------------------------\n\n")
   print(f"\t\t\t\t\t ~(~p)     ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print("\t\t\t\t\t~(~",p[i],")                           |", (not(not(p[i]))))
   
  
   
  
  elif choice==5:
   print("enter 1 or 0 for q:")
   for i in range(size):
     d=int(input())
     print(bool(d))
     q.append(bool(d))
   print("the boolean you choose for q is:",q)
   print("enter 1 or 0 for r:")
   for i in range(size):
     e=int(input())
     print(bool(e))
     r.append(bool(e))
   print("the boolean you choose for r is :",r)
   print("\t\t\t\t\t------------------------------\n")
   print("\t\t\t\t\t5.)   ASSOCIATIVITY LAW ")
   print("\t\t\t\t\t------------------------------\n\n")
   print("\t\t\t A.) (p ^ q) ^ r = p ^ (q ^ r)\n")
   print(f"\t\t\t\t\t(p ^ q) ^ r     ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print(f"\t\t\t\t\t({p[i]} \t^ {q[i]}) ^ {r[i] }                 |{(p[i] and q[i])and r[i]}")
   
   print(f"\n\t\t\t\t\tp ^ (q ^ r)   ")
   print("\t\t\t\t\t------------------------------\n")
   
   for i in range(len(p)):
     print(f"\t\t\t\t\t{p[i]} \t^ ({q[i]} ^ {r[i] })                  |{p[i] and (q[i]and r[i])}")
   print("\t\t\t\t\t------------------------------\n\n")

   print("\t\t\t B.) (p or q) or r = p or (q or r)\n")
   print(f"\t\t\t\t\t(p or q) or r     ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print(f"\t\t\t\t\t({p[i]} \tor {q[i]}) or {r[i] }                 |{(p[i] or q[i])or r[i]}")
   
   print(f"\n\t\t\t\t\tp or (q or r)   ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print(f"\t\t\t\t\t{p[i]} \tor ({q[i]} or {r[i] })                  |{p[i] or (q[i]or r[i])}")

  elif choice==6:
   print("enter 1 or 0 for q:")
   for i in range(size):
     f=int(input())
     print(bool(f))
     q.append(bool(f))
   print("the boolean you choose for q is:",q)
   print("\t\t\t\t\t------------------------------\n")
   print("\t\t\t\t\t6.)   DEMORGANS LAW ")
   print("\t\t\t\t\t------------------------------\n\n")
   print("\t\t\t\t\t~(p ^ q) = ~p or ~q     ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print("\t\t\t\t\t~(",p[i]," \t^ ",q[i],")\t->>", (not (p[i] and q[i])),"  \t=\t ",(not p[i])," or ",(not q[i]),"             ->>",(not(p[i]) or (not(q[i]))))
   
   print("\n\t\t\t\t\t~(p or q) = ~p and ~q    ")
   print("\t\t\t\t\t------------------------------\n")
   for i in range(len(p)):
     print("\t\t\t\t\t~(",p[i]," \tor ",q[i],")\t->>", (not (p[i] or q[i])),"  \t=\t ",(not p[i])," and ",(not q[i]),"               ->>",(not(p[i]) and not(q[i])))

  elif choice==0 :
    exit()   