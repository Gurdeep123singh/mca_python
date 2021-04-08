'''  This is a program of prime and composite no where it gives length 
     and list of prime no.'s and composite no.'s
 --->>>>>   HERE WE ARE TAKING N TERMS list from user by element wise FROM WHICH WE FIND PRIME AND COMPOSITE
           NO LIST  
 
 
 ->> here we are comparing and by use of bool function we are giving output
 ->> without using return function
 i/p - enter upto which n term you want prime and composite no.'s  ex -7
  ->> enter element 1: 10
      enter element 2: 3
      enter element 3: 15 ....etc
     ex:- list of  7 elements are: [10,3,15,6,7,9,4]

 i/p - enter upto which n term you want prime and composite no.'s  ex -10
 o/p - 2 prime no.'s :-[3,7]   5 composite no.'s :- [10,15,6,9,4]

'''

def prime_composite(list_of_elements):  # defining composite fn
 b=[]    # empty list  # FOR APPENDING PRIME NO.'S IN THE LIST
 c=[]    # empty list  # FOR APPENDING COMPOSITE NO.'S IN THE LIST
 
 for i in list_of_elements:  # TAKING LIST OF ELEMENTS WHICH USER HAS GIVEN
     flag =True
     for j in range(2,i-1):  # for checking  that if  i  divides by (2,i-1)
         if (i % j == 0):   # comparing if by dividing it gets 0 then it is composite no not prime as prime is- 
             flag = False    #   divisible by itself and 1
             break           # the instant it gets false it breaks and it goes to false part and there appends and then again comes for another no to check

     if (flag == True):  # if true then it appends in list of b
         b.append(i)
        
     if (flag == False):    # if false then it appends in list of c
         c.append(i)
     
 print("The ",len(b)," prime nos are :\t",b)     # gives length with list of prime no.'s
 print("The ",len(c), " composite no.'s are :\t",c)   # gives length with list of composite no.'s
 print("Total prime no.'s from 1 to", len(list_of_elements) ,"are :   ",len(b))
 print("Total composite no.'s from 1 to",len(list_of_elements)," are :   ",len(c))

def main():  # defining main fn
 list_of_elements = []
 number = int(input("enter length of list from which you want to decide either no is prime or composite : "))
 for i in range(0,number):
     print("enter element ",i+1)
     c=int(input())    # taking input in c one by one
     list_of_elements.append(c)   # appending elements in list
     print("the given elements are: ",list_of_elements)
 prime_composite(list_of_elements)   # calling prime fn        

main()    # calling main fn 