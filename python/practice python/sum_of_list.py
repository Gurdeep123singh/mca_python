'''
program to give sum of two lists by taking list from user 
and returning sum of list 
'''
def sumTwoNum(x,y):  # doing sum 
 z=[]
 for i in range(len(x)):
     c=x[i]+y[i]
     z.append(c)
 return z  # returning sum of list

def sumList():  # taking inputs in the list
 n= int(input("enter a no upto which elements you want to stored in a list :"))
 l1=[]
 l2=[]
 print("enter elements in the list1")
 for i in range(n):    
     c=int(input())   # taking input
     l1.append(c)  # appending list

 print("enter elements in the list2")
 for i in range(n):
     c=int(input())  # taking input
     l2.append(c)   # appending list

 z=sumTwoNum(l1,l2)
 print("elements of list 1: ",l1) # printing list of elements
 print("elements of list 2:",l2)   # printing list of elements

 print("sum of list: ",z)  # printing sum of list which is returning from sumTwoList


sumList()   # calling sumList() 

