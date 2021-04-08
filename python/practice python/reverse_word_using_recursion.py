'''
program to have reverse of string using recursion
by taking two list 1st list for string append and other for reverse storing and then reverse list to string
i/p :- hello
o/p:- olleh

'''
def reverse1(list1,result):           # have list1 and result as a parameter
 if list1!=[]:                        # it will return till list1 is not empty
     result.append(list1[-1])         # and last elements to 1st element is stored in result list recursively
     list1.pop(-1)                    # and last element is poped recursively till 1st element 
     reverse1(list1,result)           # recursion
     return result                   # returning result of reverse string
 else:                               # if list empty returns result of reverse string
     return result    

def main():                                         # defining main fn
 string=input("ënter the string to reverse\n")
 
 for i in string:                                    # string is appended in list1
     list1.append(i)
 reverse=reverse1(list1=[],result=[])                 # calling reverse fn for returning reverse of string
 string=""
 for elements in reverse:                     # then changing list to string
     string+=elements
 print('reverse of the string is :',string)

main()                                           # calling main fn

