'''
program to find flattening of list i.e. multidimensional list to 1 d list
i have used 3 functions with return i.) flattening :- where flattening of list is there ii.) multidimension_list :- where
it gives list as same the user gives , we take list as a string and split it and then it gives the list iii.)
main :- where calling of both fn and printing is taken 
i/p :- [1,[[2,3],4],5]
o/p :- [1,2,3,4,5]
'''

def flattening(old_list,new_list):
    if old_list==[]:                                # if old list is empty returns new list
        return new_list
    elif type(old_list[0]) is list:                 # if 1st element is list 
        flattening(old_list[0],new_list)            # then we have to send it again for nested loop elements append 
        flattening(old_list[1:],new_list)           # and after 1st element all elements are send to check for
    else:
        new_list.append(old_list[0])                # if 1st element is not list then it is apended in the list
        old_list=old_list[1:]                       # and after 1st element all elements are send to check for
        flattening(old_list,new_list)               # again calling for checking other elements
    return new_list                                 

def multidimension_list(Input,List=list()):
    if Input == []:                                    # if user list is empty simple returns the new list
        return List
    elif Input[0] ==']':                              # if users 1st element is ] then remove it
        Input.pop(0)
        return List 
    elif Input[0] =='[':                              # if users 1st element is [ then remove it and append nested
        Input.pop(0)                                 # loop also
        
        List.append(multidimension_list(Input,List=list()))       # for nested loop
        
        return multidimension_list(Input,List)                   
    else:
        List.append(Input[0])                       # adding element to list if element is not [ or ] 
        Input.pop(0)                                # remove the first element from users list
        
        return multidimension_list(Input,List) 

def main():
 print("please enter the list (of any dimension) ")
 print("*******by entering the element and square bracket********\n please keep space between them ")
 print('like :-  1 [ 2 [ 3 [ [ 4 ] ] 5 ] 6 ] \n')
 Input=input('enter the list: ')                   # taking input from user
 spliiting=Input.split()                           # splitting the elements according to your space  
 list1=multidimension_list(spliiting)                            # calling the function  and put into list1
 print('the entered List is ->>>\t',list1)

 
 print(f"your 1d list is :{flattening(list1,new_list=list())}")     # calling the flattening fn
 
main()                                                                 # calling main fn



