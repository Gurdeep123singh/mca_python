'''
Program to implement tower of Hanoi iteration
start has all disk
end where all disks have to send
mid to help for moving disk from start to end
'''          

def main():
    no_disks=int(input('Enter the number of disks: '))                                      # taking input from user for number of disk
    start=[j for j in range(no_disks,0,-1)]                                                # start tower
    end=[]                                                                       # end tower
    mid=[]                                                                               # mid tower
    move=2**no_disks-1                                                                      # no of  moves 
    
    print(f'Soure Tower ---> {start}\nDestination Tower ---> {end}\nmid Tower ---> {mid}') 
    print('Note: disk get smaller when go from left to right i.e LIFO') 
    print('Total number of move Required: ',move)                                            
    print('\nStep:\n')
    hanoi_iteration(start,end,mid,move,no_disks)                                    # class function to print steps for tower of hanoi


def hanoi_iteration(start,end,mid,move,no_disks):                              # fn for hanoi tower
    
    for i in range(1,move+1):
        if i%3==1:                                                                        # move disk from start to end or vice versa                                     
            if end==[]:                                                           # empty
                end.append(start[-1])                                              # move top disk from start to end
                start.pop()
            
            elif start==[] or start[-1]>end[-1]:      
               
                start.append(end[-1])                                            # move top disk from end to start
                end.pop()
            elif end[-1]>start[-1]:
                
                end.append(start[-1])                                           # move disk from end tower to start tower
                start.pop()

        elif i%3==2:                                                             # move disk from mid tower to start or vice versa 
            if mid==[] :                                                        # empty
                
                mid.append(start[-1])                                            # move top disk from start to mid tower
                start.pop()
            
            elif start==[] or start[-1]>mid[-1]:
                         
                start.append(mid[-1])                                          # move disk from mid tower to start 
                mid.pop()
            elif mid[-1]>start[-1]:  
                
                mid.append(start[-1])                                          # move top disk from start tower to end
                start.pop()

        elif i%3==0:                                                          # move disk from end tower to mid  or vice versa
            if end[-1]>mid[-1]:    
                
                end.append(mid[-1])                                 # move top disk from mid tower to end
                mid.pop()
            elif mid[-1]>end[-1]:  
                
                mid.append(end[-1])                                 # move top disk from end tower to mid
                end.pop()

        if no_disks % 2 ==0:                                            #  even disk
            print(f"step {i}:\nStart Tower ---> {start}\nend Tower ---> {mid}\nmid Tower ---> {end}\n")
        else:                                                           # disk is odd
            print(f"step {i}:\nStart Tower ---> {start}\nend Tower ---> {end}\nmid Tower ---> {mid}\n")

main()                                                        # calling function 
