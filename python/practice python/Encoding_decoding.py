'''
program to make encoding and decoding by using functions and return
i/p :- 12sdA@
encoded:-******* ENCODING PART IS ********
 eno owt 511 001 56 @
 decoded:-******* DECODING PART IS ********
12sdA@

'''
import os                   # import for checking if file exists or not
dict1={1:"one", 2: "two", 3: "three", 4: "four",5: "five",6: "six",7: "seven", 8: "eight",9: "nine", 0: "zero"}

def encoding(msg):                               #  encoded section
    c=[]
    
    for i in msg:                                # msg goes in i one by one
        if i.isdigit():                          # if digit
            c.append(dict1[int(i)][::-1])        # from dictionary it takes its value and appends in reverse

        elif i.isalpha():                        # if alphabet
            
            a=str(ord(i))                        # makes it ascii code
            c.append(a[::-1])                    # appends ascii in reverse form
        else:
            c.append(i)                          # if space or special char simply appends
                

     
    d=' '.join(c)                                     # makes list into string
    return "******* ENCODING PART IS ********\n " + d     # returning encoded part

def decoding(msg):                                    # decoded section
    
    if msg!='':                                       # if not space then split
        e=msg.split()
        
    
    d=[]
    reverse = {value: key for key, value in dict1.items()}       # making 'one' as key and '1' as value in reverse dictionary
    
    for i in range(len(e)):             # reverse encoded are stored in d as original form                         
     d.append(e[i][::-1])
    

    f=[] 
    for j in range(len(d)):           
     if d[j] in reverse:                    # taking values from reverse dictionary 
         f.append(str(reverse[d[j]]))     
     elif d[j].isdigit():                # if digit then make ascci as char
         f.append(chr(int(d[j])))
     else:
         f.append(d[j])                 # simply append space and special character
    g=''.join(f)
    return "******* DECODING PART IS ********\n" + g         # returning decoded part
                 
    

while True:
    
 option=input("\t\twhat you want to do: encoded(e) or decoded(d) or exit(q)")   #  asking options
 
 
 
 if option=="e": 
     msg=input("enter msg:")                        # for encoded
     encoded_code=encoding(msg)           # calling for returning encode
     print("the encoded part is :",encoded_code)
 elif option=='d': 
     msg=input("enter msg:")                              # for decoded
     decoded_code=decoding(msg)                    # calling for returning decode
     print("the decoded part is :",decoded_code)
 elif option=='q':                                             # otherwise exits
     exit()                         
