''' A recursion program in which 1 reverse string using recursion
and then using reverse string and original string as a parmeter in palindrome_check
i find palindrome recursion by seeing characterwise from starting'''s



def reverse1(list1,result):     
 if list1!=[]:
     result.append(list1[-1])
     list1.pop(-1)
     reverse1(list1,result)
     return result
 else:
     return result    

def palindrome_check(string1,string):
 if string1=="" and string=="":
     return True  
 elif string1[0]==string[0]:
     string1=string1[1:]
     string=string[1:]
     palindrome_check(string1,string)
     
 elif string1[0]!=string[0]:
     return False 
     


string="121"
list1=[]
result=[]
for i in string:
    list1.append(i)
reverse=reverse1(list1,result)
string1=""
for elements in reverse:
 string1+=elements
print('reverse of the string is :',string1)

status=palindrome_check(string1,string)
if status==True:
    print(f"yes {string} is palindrome ")
else:
    print(f"no {string} is not palindrome ")    



