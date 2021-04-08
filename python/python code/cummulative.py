def Cumulative(list1):  # function for cummulative

    cummulative_list = []

    length1 = len(list1)   # taking list

  # adding 0 to 0 elements , 0 to 1 elements, 0 to 2 , 0 to 3 , till length
  #and storing in cumm_list'''
    cummulative_list = [sum(list1[0:i]) for i in range(0, length1+1)]
                                
    return cummulative_list[1:] # returning list of cummulative freq. to main

def main(): 
 n=int(input("give no of elements:  "))  ## taking no of elements
 list1 = []
 for i in range(0,n):  # 0 to no of elements
     print("enter element no  ".format(i+1)) # gives element no 1,2 etc
     element1 = int(input()) # taking elements till n
     list1.append(element1)  # then appending elements in empty list
 print("the entered list is:  \n",list1)    
 print (Cumulative(list1))  # printing cumulative list

main()  # calling main function
