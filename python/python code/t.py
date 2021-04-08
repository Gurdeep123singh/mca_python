a = int(input("enter no. of fruits"))
b=[]

for i in range(1,a+1):
   c=input("give nam of fruit")
   b[i]=c[i]   
print("the fruits are:",b)    
  

  
s = input("enter the string")


def largest(s):
 split1 =[] # empty array for list 
 split2 =[] # empty array for list
 temp =''
 for c in s:
     if c == ' ':
         split1.append(temp)
         temp =''
     else:
         temp += c
 if temp:
     split1.append(temp)            
 print(split1)

 for i in split1:
    split2.append(len(i))
  maximum =max(split2)

 for i in split1:
    if(len(i)==maximmum):
       print(i)  


 

