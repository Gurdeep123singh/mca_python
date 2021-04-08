'''
1           ->  how many example have to take
3 10        -> 3  types of stones are there  and 10 is max time to pick up stone at a time
3 4 5       -> this line gives no of stones of each types i.e. 1st type has 3 stones , 2nd type has 4 stones ,3rd type has 5 stones 
4 4 5       -> this is profits for each type of stones i.e ist type of stones has rate 4,..... 
12          -> o/p :- 12 max profit gained by picking max stones in max time 

map(int,input().split())  -> means string ko split karega and change in int if string has int input 
'''
t = int(input())
for _ in range(t):
    n,k = input().split()
    a_s = map(int,input().split())   # has no of stones of each types i.e. 1st type has 3 stones , 2nd type has 4 stones ,3rd type has 5 stones
    b_s = map(int,input().split())
    print(max(map(lambda ab: ab[1]*(int(k)//ab[0]),zip(a_s,b_s))))  # ab[0]  = a_s  # ab[1] = b_s # // gives integer value 
    # int(k) -> time ko divide kr rahe ha by no of stones                    