'''program to find shallow copy using recursion 
->> here we are appending list1 elements in list2 and by this the id is  same of list1 and list2 .
 If we change the value of list1 there is  change in list2 also.
i/p :- [1,2[[3,4],5],6]
o/p:- before change
list1 =  [1,2[[3,4],5],6]
list2 =  [1,2[[3,4],5],6]
after change:- suppose from 3 to a
list1 =  [1,2[[a,4],5],6]
list2 =  [1,2[[a,4],5],6]

'''


def shallow_copy(list1,list2): 
 while list1 != []:                           # if list is not empty
   list2.append(list1[0])                    # append list1 elements in list2 by this list1 and list2 has same id
   list1=list1[1:]                           # from 2nd element to length of string in list1
   shallow_copy(list1,list2)
   return list2
 return list2                               # returning list2
   
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


def main():                  # defining main fn
 
 print("please enter the list (of any dimension) ")
 print("*******by entering the element and square bracket********\n please keep space between them ")
 print('like :-  1 [ 2 [ 3 [ [ 4 ] ] 5 ] 6  \n')
 Input=input('enter the list: ')                   # taking input from user
 spliiting=Input.split()                           # splitting the elements according to your space  
 list1=multidimension_list(spliiting)              # calling the function  and put into list1
 
 print("Before change ->>")
 print('List 1 is ->>>',list1)
 
 list2=shallow_copy(list1,list2=[])
 print('list2 is :',list2)
 
 # for checking if deep copy is working in nested loop(only for 2d change)

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
 print('list 2 is',list2)

main()                            # calling main fn

