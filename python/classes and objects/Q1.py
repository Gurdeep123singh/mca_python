def main():                                              # main fn
    a = int(input("enter no. of rows"))          
    print('pattern_type of right triangle')
    pattern_type=input('squares(s) or simple(q)')
    right_triangle(a,pattern_type)


def right_triangle(a,pattern_type):
    if pattern_type=='q':
        for i in range(1,a+1):  # 1 to rows+1
            for j in range(1,i+1):  # 1 to 1 , 1 to 2 , 1 to 3
                print(i, end = "")    # prints rows values in col 
            print()  
    
main()