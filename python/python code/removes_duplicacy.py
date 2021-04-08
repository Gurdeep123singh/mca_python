def Removing(list1):  # function for removing duplicacy

    list2 = []  # make empty list

    for i in list1:  #list1 elements goes in i  

        if i not in list2: # it sees if 1 is in list not then fill it with 1, then sees for another 1 it see 
                            # that it is there so it doesnot fill
            list2.append(i)  # list2 i.e. final list is append with i

    return list2   # returning list2 in main


def main(): 
 n=int(input("give no of elements:  "))  ## taking no of elements
 list1 = []
 for i in range(0,n):  # 0 to no of elements
     print("enter element no  ".format(i+1))  # gives element no 1,2 etc
     element1 = int(input())  # taking elements till n
     list1.append(element1)  # then appending elements in empty list
 print("the entered list is:  \n",list1)    
 print(Removing(list1))  # printing removing duplicacy list

main()  # calling main function



      
