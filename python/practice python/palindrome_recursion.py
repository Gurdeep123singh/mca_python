''' program to check whether given string is palindrome or not using recursion
by checking status if status is true then yes it is palindrome 
otherwise not
i/p :- 121
o/p :- yes palindrome
'''

def palindrome(string):                            # taking string as a parameter
    if string=='':                                 # if string empty 
        return True                                # returns true as it is palindrome
    elif string[0]!=string[len(string)-1]:        # checks 1st element and the last element of string
        return False                                 
    elif string[0]==string[len(string)-1]:       # checks 1st element and the last element of string
        string=string[1:len(string)-1]         # if yes then 2nd element to second last element is stored in string
        palindrome(string)
        return True

def main():                                                                       # defining main fn
 string= input("enter the string to check whether it is palindrome or not->>>\n")
 status=palindrome(string)                      # true or false is stored in status
 if status == True:                              # if true
     print(f"{string} is palindrome")
 else:                                           # if false
     print(f"{string} is not palindrome")  

main()                                            # calling main fn
