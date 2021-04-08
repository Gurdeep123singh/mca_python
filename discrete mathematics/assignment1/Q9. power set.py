'''
program to make power set recursively
'''
def power_set(l):
    # Iteratively take one and 'merge'
    
    ps = [l]                                            # ex - 1234 as [1234] in power set
    for i in range(len(l)):
        for y in power_set(l[:i] + l[i + 1:]):           # making elements in power set
            if y not in ps:                              # if elements of power set is not in power set 
                ps.append(y)
    return ps                                            # returning power set


set_size= int(input("enter size of set:"))           # taking size of set
set1=[]
print("enter elements for set:")
for i in range(set_size):                                # appending elements  for set1
    set1.append(input())  
print("power set is : \n",power_set(set1))                                                  # calling fn power set
print("length of power set: ",len(power_set(set1)))
