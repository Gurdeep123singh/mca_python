f=open('1.txt',mode='r')
no=input("which no you ")
index=0
p=[]
for x in f:
    for i in x:
        if i=='['  :
            newstr=x.replace('[','') 
            newstr.strip()
            print(newstr)
            if newstr==']':
                newstr1=x.replace(']','') 
                newstr1.strip()
                print(newstr1)

          
            
            
    #     if no in i:
    #         print("index is at :",index)
    #     else:
    #         pass    
    #     index+=1
    # print("no. not found")    
      
   
    