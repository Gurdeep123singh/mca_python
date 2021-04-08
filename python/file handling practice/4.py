import numpy as np
import os
import pickle
def writing(filename,content,mode='w'):
    if(os.path.exists(filename)):                    # checking if file exists
        print("\nfile already exists!!!!\n")
        return False                                       # status = false
    else:
        f=open(filename,mode)                          # if file not exists then create it and write in it

        
        
        pickle.dumps(content,f)                                 # writing content
        f.close()           

def reading(filename,mode='r'):
    try:
        f=open(filename,mode)
        for x in f:
            np.array(x)
            print(int(x))

    except IOError or UnboundLocalError:                     # if file doesnt exists or UnboundLocalError
        
        print("\nfile doesnt exists or doesn't has input!!\n")

def searching(filename,no,mode='r'):
    try:
        f=open(filename,mode)
        
        count=0
        for x in f:
            for i in x:
                if no in i:
                    return count  
                else:
                    pass    
                count+=1
        
    except IOError or UnboundLocalError:                     # if file doesnt exists or UnboundLocalError
        
        print("\nfile doesnt exists or doesn't has input!!\n")
   
    return -1

def main():
    
    
    while True:
        print("\nyou want to write in a file or read  ")
        print('If write (w) or read (r) or search (s) or exit (e) :::')
        option=input()
        if option=='w':
            
            print("how many no you want to put in a file: ")
            no=int(input())
            print("enter no's you want to put ")
            list1=[int(input()) for i in range(no)]
            nos_in_1d=(np.array(list1))
            print(nos_in_1d)

            print("enter filename where you want to write : ")
            filename=(input() + '.txt')
            status=writing(filename,nos_in_1d)
            if status!=False:
                print(f"{filename}.txt is created !!!")    
        
        elif option=='r':
            filename1=(input("enter filename which you want to read without extension ") + '.txt')
            reading(filename1,mode='r')
            
        elif option=='s':
            print("from which file you want to search no.  ")
            filename=(input("TELL US THE FILENAME without extension ") + '.txt')
            no=input("enter which no you want to found")
            index=searching(filename,no,mode='r')
            if index!= -1:
                print(f'{no} is at index :{index} ')
            else:
                print("NO. NOT FOUND !!!!!")   


        elif option=='e':
            exit()        

main()    