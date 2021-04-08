def merge_sort_ascending(list1):
    if len(list1)>1:              # if length is less than 1 then no more splitting
        mid=len(list1)//2
        left_side=list1[:mid]
        right_side=list1[mid:]

        merge_sort_ascending(left_side)   # recursively call till single elements splitted in list
        merge_sort_ascending(right_side)

        i=j=k=0

        while i<len(left_side) and j<len(right_side): # while is used because for each line having right and left list
            if left_side[i]<right_side[j]:           # comparing
                list1[k]=left_side[i]
                i+=1
            else:
                list1[k]=right_side[j]
                j+=1
            k+=1
        
        while i<len(left_side):           # if left_side elements left in upper while loop 
            list1[k]=left_side[i]
            i+=1
            k+=1
        while j<len(right_side):           # if right_side elements left in upper while loop
            list1[k]=right_side[j]
            j+=1
            k+=1    

def merge_sort_descending(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_side=list1[:mid]
        right_side=list1[mid:]

        merge_sort_descending(left_side)   # recursively call till single elements splitted in list
        merge_sort_descending(right_side)

        i=j=k=0

        while i<len(left_side) and j<len(right_side): # while used for each line having right and left list
            if left_side[i]>right_side[j]:           # comparing
                list1[k]=left_side[i]
                i+=1
            else:
                list1[k]=right_side[j]
                j+=1
            k+=1
        
        while i<len(left_side):           # if left_side elements left in upper while loop 
            list1[k]=left_side[i]
            i+=1
            k+=1
        while j<len(right_side):           # if right_side elements left in upper while loop
            list1[k]=right_side[j]
            j+=1
            k+=1    

def main():       
    size=int(input("ENTER SIZE OF LIST "))
    list1=[int(input()) for i in range(size)]
    while True:
        option=input("what type of order you want : ->\t ASCENDING(a) or DESCENDING(d) or exit(e): ").lower()
        if option=='a':
            merge_sort_ascending(list1)
            print('ASCENDING ORDER LIST IS -> ',list1)
        elif option=='d': 
            merge_sort_descending(list1) 
            print('DESCENDING ORDER LIST IS -> ',list1) 
        elif option=='e':
            exit()
        else:
            print("!!!INVALID OPTION!!!")  

main()
