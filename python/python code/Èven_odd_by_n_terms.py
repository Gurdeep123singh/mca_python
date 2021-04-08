'''  This is a program of even and odd no where it gives length 
     and list of even no.'s and odd no.'s.

   --->>>>>   HERE WE ARE TAKING N TERMS FROM WHICH WE FIND ODD AND EVEN NO LIST  
 
 ->> here we are using % 2==0(if even) otherwise odd 
 ->> without using return function

 i/p - enter upto which n term you want even and odd no.'s  ex -10
 o/p - 5 odd no.'s :-[1,3,5,7,9]   5 even no.'s :- [2,4,6,8,10]
 and giving length also.. with stmt 5 odd no's are:[1,3,5,7,9] ..

'''



def main(): # defining main fn
    number = int(input("enter N terms from which you want to decide either no is odd or even : "))
    

    ev_od(number)   # calling function


def ev_od(number):
    a=[]  # used for appending even no.'s 
    b=[]  # used for appending odd no.'s 
    
    for i in range(1,number+1):   # going from 1 to n+1 i.e. 10
        if(i%2==0):   # if divides by 2 gives remainder 0 then it appends that element and that is even no
           a.append(i)
        else:
            b.append(i) # else appends odd no.'s
    print("the ",len(a), "even no.'s are :",a)       # giving length and even no.'s list 
    print("the ",len(b), "odd no.'s are :",b)        # giving length and odd no.'s list 

main()  # calling main fn