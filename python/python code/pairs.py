'''  THIS IS A PROGRAM TO FIND  PAIRS FROM USERS LIST BY HIS GIVEN SUM 
->>> Taking  length of list then taking element one by one till length of list and then taking sum 
and finding pair for the sum from users list....
-->>>> example :- I/P :- length(n) = 4  sum(m) = 6
['1','2','3','4'] 

 o/p :- [(2,4)]
 this program doesn't returns and prints in the function only

'''

def main():  # defining main fn
 list_of_elements = []
 n = int(input("enter length of list from which you want to make pairs : "))
 for i in range(0,n):
     print("enter element ",i+1)
     c=int(input())           # taking input from user
     list_of_elements.append(c)    # appending values in list 
 print("list of elements selected by user are: ",list_of_elements)    
 m = int(input("enter sum to make pair from list of n elements : "))
 print("your chosen sum is: ",m)
 pairs(list_of_elements,m)   # calling prime fn 

def pairs(list_of_elements,m):  # taking arguments list of elements and sum of pair from main function by user
    new=[]                      # empty list
    d= len(list_of_elements)    # taking length of list
    for i in range(d):          # taking length of list in row
        for j in range(d):        # taking length of list in col
            a,b = list_of_elements[i] ,list_of_elements[j]   # taking values on indexes of row and col in a and b
            if a + b == m and i!=j:        # row +col and they are not on same indexes                   
                c=(a,b) if b>a else (b,a)   # giving (a,b) if b>a otherwise (b,a)
                if c not in new:            # if pair is not in list it appends
                    new.append(c)              
              
    print("The pairs are: ",new)          # printing list values
main()                                    # calling main 