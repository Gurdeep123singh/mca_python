'''
program to make pascal
'''
def fact(num):
    if num==1 or num==0:                            # if num=1 or 0 return 1
        return 1
    else:                                         # if greater than 1 then factorial of number
        return num*fact(num-1) 

def main():
    row=int(input("enter no of rows:"))
    for i in range(row):
        for j in range(row-i):                  # making spaces
            print(" ",end='')          
        for k in range(i+1):                           # printing values
            pascal=fact(i)/(fact(i-k)*fact(k))          # using combinations
            print(int(pascal),'' ,end='')             # used'' to have some space between elements
        print()                                      # print for outer loop
main()                                                 # calling main fn