'''
program to make sum of square of n natural no by asking user upto which no the user wants to have 
By using recursion and returning it in main fn 
i/p :- 5
o/p:- 1 + 4 + 9 + 16 + 25
      sum = 55
'''
def sum_of_squared_natural_no(no,b,sum):   # fn of doing square and sum using recursion
    while b<=no:                           # runs upto n i.e. no
        square=b*b                         # doing square
        sum+=square                        # doing sum
        b+=1                               # incrementing b
       
        sum_of_squared_natural_no(no,b,sum)          # recursive 
        
        
    return sum                                             # returning sum

def main():                                                 # main fn
    no=int(input("upto which no\n you want to have sum of squared natural no."))

    s=sum_of_squared_natural_no(no,b=1,sum=0)                                       # calling fn 
    squared_no_list=[i*i for i in range(1,no+1)]                                  # containing squared_no list 
    list1=[]
    for i in squared_no_list:                                  # appending squared no with + sign 
        
        list1.append(i)
        if squared_no_list[-1]!=i:                            # for doesn't put + sign in last
            list1.append("+")
    print('\t\t\t',*list1)                                    
    print(f"sum of squared {no} natural no's is : {s}")




main()