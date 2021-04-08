'''
program to make a synoymn from existing dictionary. 
returning is there
here we use 2 functions one is main where we are giving dictionary explicitly an printing
the synonymn ictionary an in other function which is synoymn where we are taking muDict dictionary items in word, meaning , we are taking meaning 
as a key an wor as a meaning of it , and then checking if meaning is in synoymn dictionary if it is not there we first making its list and then entering word 
by using append for adding full string of it not character and if meaning is already there we simplyy appending word for the value of meaning. 

'''
def synoymn(myDict):                         # defining function to make synoymn dictionary
    
    synoymn={}                              #  synoymn as a dictionary
    for word,meaning in myDict.items():      # giving myDict items into word, meaning
        if meaning not in synoymn:           # if meaning as akey is not there in the synoymn dictionary
            synoymn[meaning]=[]              # synomns key's values list
            synoymn[meaning].append(word)    # putting word as a value of a meaning(key) 
        else:                                # if meaning as a key is already there in synoymn dictionary it appends new value of the key 
            synoymn[meaning].append(word)   
    return synoymn                             # returning synoymn dictionary

def main():                                      # defining main fn for passing dictionary(myDict) and for calling synoymn function 
 myDict={'happy':'cheerful','merry':'cheerful','wistful':'sad','sorry':'somber','bitter':'sad'} 
 print('dictionary of synoymn from given dictionary is :')         # calling synoymn function
 
 new_dictionary=synoymn(myDict)                    # calling synonymn function and storing into new_dictionary
 for word,meaning in new_dictionary.items():       # key and value goes into word , meaning
     print(word," : ",end="")                       # prints word : 
     print(*meaning,sep=',')                        # prints meaning without [], '' so we are using split=','
                                                    # so tme meanings are splited with ,
                                                    # unpacks the meaning
main()                                            # calling main function

