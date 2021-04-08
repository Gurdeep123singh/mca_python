# This is a program of frequency  of items and index of it  
# where it takes length 
#      and list of items by user.

#    --->>>>>   HERE WE ARE TAKING N TERMS list from user by element wise in LIST  
 
#  ->> here we are using dictionary as we want item : frequency 
#  ->> with using return function

#  i/p - enter upto which n term   ex -8
#   ->> enter element 1: 1
#       enter element 2: 2
#       enter element 3: 3 ....etc
#      ex:- list of  7 elements are: [1,2,3,2,3,1,1,1]
#  o/p -  1 : 4 : [1, 6, 7, 8]
#         2 : 2 : [2, 4]
#         3 : 2 : [3, 5]
# 
#  and also gives the position of item:
# 
#         the indexed values on 1 : is: [1, 6, 7, 8]
#         the indexed values on 2 : is: [2, 4]
#         the indexed values on 3 : is: [3, 5]
# 

def main(): # defining main func
    no = int(input("how many no you want to take in the list : ")) # taking value of n
    l1=[]
    for i in range(0,no):  
      print("enter element",i+1," : ")
      c=int(input())  # taking input
      l1.append(c)    # appending element in the list
    print("the entered elements in the list :",l1)
    dictionary_elements=freq(l1)  # calling freq func and putting value in the dictionary_elements
    print("the key , value and an index of an item is : ")
    for key,value in dictionary_elements.items():  # putting items in key and value variable
        print(f"{key} : {value[0]} : {value[1]}")   # key gives item of list :value[0] gives freq : value[1] gives indexes of an item
    print("the position of an item is : ")    
    for key,value in dictionary_elements.items():  # giving key : postion of an index
      print(f"the indexed values on {key} : is: {value[1]}")


# defining func
def freq(l1):
 # initializing dict to store frequency of each element
 elements_count = {}
 index=1  # index starts from 0 so we makes starting index as 1
 # iterating over the elements for frequency
 for element in l1:
     # checking whether it is in the dict or not
     if element in elements_count:
        # incerementing the count by 1
         elements_count[element][0] += 1  # if element is there it increases frequencies in 0th postion of dictionary
         elements_count[element][1].append(index) # if element is there it appends index in 1th postion of dictionary

         
     else:
        # setting the count to 1
         elements_count[element] = [1 , [index]] # when no element in dictionary it puts item in dict with having starting value as 1 and has index also
     index +=1 # incrementing indexes  
 # printing the elements frequencies
 dictionary_elements={key:value for key, value in elements_count.items()} # putting items in dictionary_elements
 return dictionary_elements  # returning dictionary_elements to main func
     
main()   # calling main function 