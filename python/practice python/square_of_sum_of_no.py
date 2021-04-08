'''
program to find the sum of power of a digits of a no
eg :- 123  1^2+2^2+3^2=14
 i have made 3 functions :-
 1.) main -> where taking number as a string from user and then appending  in the list. andd printing values of
 square of digits in the list. and sum of the square of the digits of a number
 2.) square( ) taking two arguments number and length of the number and doing squares of the digits and
    appending in the list and returning to the main fn
 3.)  square_sum() ->   taking two arguments sqd_number list and length of the number and doing sum of the 
 squares of digits of the number and returning to the main fn

'''
def main():                               # defining main fn
 number = input("enter the number :")    # taking number from user  as a  string
 list1=[]
 for i in range(len(number)):            # going upto length of string
     list1.append(number[i])              # appending digits as a string in the list 
 print("numbers are putted in the string form",list1)    # showing list of digits of a number
 length=len(list1)                                     # storing length of list in length
 sqdNumber=square(list1,length)                     # storing list of squares of a digit in sqdNumber
 print("the square of the digits in the number are :",sqdNumber)  # printing squares of digits of list 

 sqdNumber_result=square_sum(sqdNumber,length)       # storing sum of squares of a digit in sqdNumber_result
 print("the sum of the square numbers is :",sqdNumber_result)    # printing sum


def square(list1,length):       # defining square functio
 sqdNumber=[]
 print("Total digits in the number are :",length)  # printing no of digits in number
 for i in range(len(list1)):   
     c=(int(list1[i])**2)     # storing squares of digit in c upto no of digits
     sqdNumber.append(c)  # appending the squares of digits in the list
 
 return sqdNumber      # returnig squares 

def square_sum(sqdNumber,length):    # defining square_sum fn
 sqdNumber_result=0                     # initialising 
 for i in range(length):
     sqdNumber_result +=sqdNumber[i]     # doing sum of squares of digits of a number
  
 return sqdNumber_result                   # returning sum

main()                                      # calling main fn