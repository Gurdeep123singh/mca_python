'''
program to make a tower of hanoi in recursive manner 
'''
def hanoi(n,start,end,middle):   # fn haning no. of discs and  start,end,mid rods
    if n<1:                          # if n is -ve so we cant able to move disks as there is no disk
        print("not able to move disk ")
        return                               # so it return with print statement
    elif n==1:                                  # if n=1 
        print(f"move {n} from {start} to {end}")       # so directly from start to end
        return
    else:                                                 # if disks are greater than 1
        hanoi(n-1,start,middle,end)                   # now n-1 disks mid rods from start rod to middle rod 
        print(f"move {n} from {start} to {end}")        # first transfer disk from start to end
        hanoi(n-1,middle,end,start)                     # now n-1 disks mid rods from  middle rod to start rod

number=int(input("enter a no of disk:"))                   # no. of disks
hanoi(number,"A","C","B")                         # a is start , b is mid and c is end rod 