'''
program to find deep copy using recursion 
->> here we are appending list1 elements in list2 and by this the id is not same of list1 and list2 .
 If we change the value of list1 there is no change in list2.
i/p :- [1,2[[3,4],5],6]
o/p:- before change
list1 =  [1,2[[3,4],5],6]
list2 =  [1,2[[3,4],5],6]
after change:- suppose from 3 to a
list1 =  [1,2[[a,4],5],6]
list2 =  [1,2[[3,4],5],6]

'''
def deep_copy(list1,list2):
 if list1 == []:                              # if list empty
     return list2                             # returns list
     
 elif type(list1[0]) is list:                                    # if ist element is list
     list2.append(deep_copy(list1[0],list2=[]))                # to make nested loop
     list1=list1[1:]                                           # then 2nd element to length in list1
     return deep_copy(list1,list2)
 else:  
     list2.append(list1[0])                                  # if no list simply appending 
     list1=list1[1:]                                          # then 2nd element to length in list1
     return deep_copy(list1,list2) 

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


def main():                            # defining main fn
 
 print("please enter the list (of any dimension) ")
 print("*******by entering the element and square bracket********\n please keep space between them ")
 print('like :-  1 [ 2 [ 3 [ [ 4 ] ] 5 ] 6  \n')
 Input=input('enter the list: ')                   # taking input from user
 spliiting=Input.split()                           # splitting the elements according to your space  
 list1=multidimension_list(spliiting)              # calling the function  and put into list1
 
 print("Before change ->>")
 print('List1 is ->>>\t',list1)
 
 list2=deep_copy(list1,list2=[])
 print('list2 is :',list2)
 
 # for checking if deep copy is working in nested loop(only for 2d)

 index1=int(input("enter index1 for change for in 1st nested loop:"))
 index2=int(input("enter index2 for change for 2nd nested loop:"))
 word=input("enter anything to change at [index1][inedx2]: ")
 if type(list1[index1])==list :                                    # if index of 1st nested loop is list
     if type(list1[index1][index2])==list:                         # if index of 2nd nested loop is list
         list1[index1][index2]=word                                # then that place it change that thing to a
     else:                                 # if no 2nd nested loop no change has to be done
         print("index is not there")        # so index is not there
          
 else:                                       # if no 1st nested loop no change has to be done
     print("index is not there:")            # so index is not there

 print("after change")            # after changing list1 and list 2
 print('list 1 is ',list1)
 print('list 2 is ',list2)

 


main()