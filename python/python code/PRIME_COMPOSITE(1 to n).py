'''  This is a program of prime and composite no where it gives length 
     and list of prime no.'s and composite no.'s.

   --->>>>>   HERE WE ARE TAKING N TERMS FROM WHICH WE FIND prime AND composite NO LIST  
 
 ->>  by dividing and by use of bool we have output 
 ->> without using return function

 i/p - enter upto which n term you want prime and composite no.'s  ex -10
 o/p - 4 prime no.'s :-[2,3,5,7]   5 composite no.'s :- [4,6,8,9,10]
 and giving length also.. with stmt 4 prime no's are:[2,3,5,7] ..

'''

def prime_composite(number):  # defining composite fn
 b=[]    # empty list  # FOR APPENDING PRIME NO.'S IN THE LIST
 c=[]    # empty list  # FOR APPENDING COMPOSITE NO.'S IN THE LIST
 
 for i in range(2,number+1):  # TAKING LIST OF ELEMENTS WHICH USER HAS GIVEN
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
 print("Total prime no.'s from 1 to", number ,"are :   ",len(b))
 print("Total composite no.'s from 1 to",number," are :   ",len(c))

def main():  # defining main fn
 
 number = int(input("enter n terms from which you want to decide either no is prime or composite : "))
 
 prime_composite(number)   # calling prime fn        

main()    # calling main fn 