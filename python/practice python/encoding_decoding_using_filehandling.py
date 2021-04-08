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

def readfile(fname,mode='r',msg="n"):                # fn for eading
    
    try:                                          # in try to check if error occurs
        
        f=open(fname,mode)                       # opening file in f
        
        if msg=='r':                               # if msg == r simply reads
            for x in f:                            # f data goes in x
                print("\nthe input in the file is : ",x,end="")   # x part is printed in one line as end=''
                
                        
                
        elif msg=='d':                                    # if d meands decoded has to do
            for x in f:
                
                print("\nthe input in the file is : ",x,end="")
                        
                decoded_code=decoding(x)                        # data goes into decode section for decoding
            return decoded_code                       # returning decoded part

        elif msg=='n':                              # if n
            for x in f:
                
                print("\nthe input in the file is : ",x,end="")
                        
                encoded_code=encoding(x)                       # data goes into encode section for encoding
            return encoded_code                               # returning encoded part


    except IOError or UnboundLocalError:                     # if file doesnt exists or UnboundLocalError
        
        print("\nfile doesnt exists or doesn't has input!!")
        return False                                           # status =false

def writing(filename,content,mode='w'):                # writing section
    if(os.path.exists(filename)):                    # checking if file exists
        print("\nfile already exists!!!!")
        return False                                       # status = false
    else:
        f=open(filename,mode)                          # if file not exists then create it and write in it

        f.seek(0)                                      # from position 0 to write
        
        f.write(content)                                 # writing content
        f.close()                                # after using file closing it


    
while True:                              # used as a option
    
 option=input("\t\twhat you want to do: reading(r) or encoded(e) or decoded(d) or quit(q): ")
 
 if option=='r':                         # if option is read only
     filename=(input("\nenter filename without extension for reading input : ")+'.txt')  # .txt to give extension by myself
     readfile(filename,mode='r',msg='r')          # callinf fn to have return
     

 
 

 elif option=='e':                                                    # encoded section
     filename=(input("\nenter filename without extension for reading input to encode : ")+'.txt')  # .txt to give extension by myself
     encode=readfile(filename)    # return encoded data 
     if encode!=False:            # if file doesnt exists or file doesnt has any input to encode
            print("\nIF YOU WANT TO ENCODING PART TO PRINT IN FILE (y) OR WANT TO PRINT IN TERMINAL (n)\n")
            msg=input("Enter yes(y) or no(n) or exit from encoding section(e) ")
            if msg=="y":             # if y then creating file with encoded part
            
                filename1=(input("\nenter filename without extension for writing encoding : ")+'.txt')
                status=writing(filename1,encode)   # calling for return encoded part
                if status!=False:                   # if file doesnt exists or file have input to encode
                    print("\nthe encoded part is done!!!!")
                
            elif msg=="n":                                # to print in terminal only
                print("\nthe encoded part is : ",encode)
            elif msg=='e':                               # exit from encoding section
                exit     

     

 elif option=='d':                                        # decoded section            
     filename=(input("\nenter filename without extension for reading file to decode: ")+'.txt')  # .txt to give extension by myself
     decode=readfile(filename,mode='r',msg='d')  # return decoded data
     
     if decode!=False:             # if file doesnt exists or file doesnt has any input to decode
            print("\nIF YOU WANT TO DECODING PART TO PRINT IN FILE (y) OR WANT TO PRINT IN TERMINAL (n)\n")
            msg=input("\nEnter yes(y) or no(n) or exit from decoded section(e)")
            if msg=="y":            # if y then creating file with decoded part
            
                filename1=(input("\nenter filename without extension for writing decoding : ")+'.txt')
                decoded_code=writing(filename1,decode)    # calling for return decoded part
                if decoded_code!=False:                    # if file doesnt exists or file have input to decode
                    print("\nthe decoded part is done!!!!")
                                
            elif msg=="n":                                  # to print in terminal only
                print("\nthe decoded part is : ",decode)
            elif msg=='e':                                  # exit from decoding section
                exit    

 elif option=='q':             # break from while loop
     exit()     

       


 
 