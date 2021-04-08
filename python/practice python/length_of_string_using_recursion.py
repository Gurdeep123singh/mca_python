'''
program to count the length of string using recursion with returning
where i have given additional  option if you want to count the length of string or characters in the string
The program is taking option from you 
i/p :- enter string :- gurdeep singh
      option->>   you want to count the length of string(a) or length of characters in the string (b) 
      if a then length of string is 13
      if b then length of string is 12


'''
def length1(string,count):     # defining length function
 list1=[]                      # initialising list
 if string=='':                # if string is empty then return list
     return count
 else:
     count=count+1                  # incrementing the count with 1
     string=string[1:len(string)]     # string is given 2nd element to length of string 
     length=length1(string,count)     # storing value in length variable
     return length                    # returning length
     
     

def main():
 string=input("enter the string\n ")
 count=0                                            # initialising count with 0
 print("option->>>you want to count the length of string(a) or length of characters in the string (b)\n")
 option=input(" enter a or b\n")
 if option == 'a':
     for i in range(len(string)):               # till length of string
         if string[i]==" ":                     # if string has space it decrements the count else not 
             count-=1
         else:
             pass
     print("length of characters in the string is :    ",length1(string,count))   # calling fn
 else:
     count=0
     print("length of string is :    ",length1(string,count))         #  calling fn

main()                                  # calling main fn