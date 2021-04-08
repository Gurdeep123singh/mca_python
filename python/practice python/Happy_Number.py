''' program to check that given no is happy or not .
    there are 3 functions:-
    1 main -> where number is taken from the user and checking whether it is happy or not 
    if it is print(yes)
    2 HappyNumber -> where it has iteration upto 10 for checking happy 
    3 sum_Square -> doing sum of squares.
    input -> 13 
    output -> 13 is a happy number


'''
def main():                                    # defining main function
    num=int(input('Enter the number'))          # taking input from user
      
    if HappyNumber(num)==True:                  # if happy print is happy
        print(num,'is Happy Number') 
    else:
        print(num,'is not Happy Number')         # otherwise not
         

def HappyNumber(num):                            #  defining happy number for checking if yes then return true
    
 result=sum_Square(num)                     # sum of squares of digits is put into result 
 for i in range(10): 
     if result==1:                      # if yes then return true
         return True 
     else:   
         result=sum_Square(result)        # otherwise again go for doing sum of power and then put into result
                                           # and then checking result for next iteration and then go on upto 10

def sum_Square(num):     # doing sum of squares of a digit of a number
 sum=0                    # initialising sum as 0    
 while num>0:              # goes on until num>0
     remainder=num%10      # taking remainder value as a last digit of a number
     sum=sum+(remainder**2)     # doing sum to the power digits of a number
     num=num//10                # taking quotient value as a num 
 return sum                     # returning sum
        
main()                           # calling main fn
