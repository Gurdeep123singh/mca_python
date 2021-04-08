'''  This is a program of even and odd no where it gives length 
     and list of even no.'s and odd no.'s.

   --->>>>>   HERE WE ARE TAKING N TERMS list from user by element wise FROM WHICH WE FIND ODD AND EVEN NO LIST  
 
 ->> here we are using % 2==0(if even) otherwise odd 
 ->> without using return function

 i/p - enter upto which n term you want even and odd no.'s  ex -7
  ->> enter element 1: 10
      enter element 2: 3
      enter element 3: 15 ....etc
     ex:- list of  7 elements are: [10,3,15,6,7,9,4]
 o/p - 4 odd no.'s :-[3,15,7,9]   3 even no.'s :- [10,6,4]
 and giving length also.. with stmt 4 odd no's are:[3,15,7,9] ..
 '''


def main(): # defining main fn
    list_of_elements = []
    number = int(input("enter length of list from which you want to decide either no is odd or even : "))
    for i in range(0,number): # going from 0 to number
      print("enter element ",i+1)
      c=int(input())    # taking input in c one by one
      list_of_elements.append(c)  # appending elements in list

    ev_od(list_of_elements)   # calling function


def ev_od(list_of_elements):
    a=[]   # used for appending even no.'s 
    b=[]   # used for appending odd no.'s 
    
    for i in list_of_elements:   
        if(i%2==0):   # if divides by 2 gives remainder 0 then it appends that element and that is even no
           a.append(i)  # if appends even no.'s
        else:
            b.append(i) # else appends odd no.'s
    print("the ",len(a), "even no.'s are :",a)       # giving length and even no.'s list   
    print("the ",len(b), "odd no.'s are :",b)         # giving length and odd no.'s list 

main()  # calling main fn