a = int(input("enter the no upto which you want to have prime no's"))
for i in range(1,a+1):
 flag =True
 for j in range(2,i-1): 
   if (i % j == 0):
    flag = False
    break

 if (flag == True):
  print("prime no.s are :", i)
 if (flag == False):
  print("composite no.s are :", i)     
