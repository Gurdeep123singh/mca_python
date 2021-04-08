def descend(list1,number):
 for i in range(number):
     for j in range(number):
         if(list1[i]>list1[j]):
             c=list1[i]
             list1[i]=list1[j]
             list1[j]=c
         else:
             pass
 return list1          
        
   

def ascend(list1,number):
 for i in range(number):
     for j in range(number):
         if(list1[i]<list1[j]):
             c=list1[i]
             list1[i]=list1[j]
             list1[j]=c
         else:
             pass
 return list1

def main():
 number=int(input("enter the no upto which you want to take elements:"))
 print("enter elements in the list :")
 list1=[]
 for i in range(number):
     c=int(input())
     list1.append(c)
 print("the list is :",list1)

 print("the ascending list is:",ascend(list1,number)) 

 print("the descending list is:",descend(list1,number)) 

main()
