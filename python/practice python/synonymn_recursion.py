'''
program to make a synoymn from existing dictionary.
returning is there 
here we use 2 functions one is main where we are giving dictionary explicitly and printing the original dictionary and
the synonymn dictionary .In other function which is synoymn where we are checking if meaning as a key is present in 
synonymn dictionary then we are simply appending synonymns of it and poping the key value from mydict
otherwise we make meaning as a new word in synonymn dictionary and then poping this key from the mydict
and when dictionary is empty it returns synoymn dictionary 

'''
def main():
    myDict={'happy':'cheerful','merry':'cheerful','wistful':'sad','sorry':'somber','bitter':'sad'}
    
    print("\nmy dictionary is ->>>>\n")

    for word,meaning in myDict.items():        # myDict key in word and value in meaning 
        print(word," : ",end="")                        # prints word : meaning   # end used for making word meaning in one line
        print(meaning)                                    # prints meaning



    print("\nmy synonymn dictionary is->>>\n")

    
    synonymn_dict={}                                  # empty dictionary
    new_dictionary=synonymn(myDict,synonymn_dict)     # calling synonymn fn and returning value is stored into new_dictionary
    
    for word,meaning in new_dictionary.items():        # new_dictionary key in word and value in meaning 
        print(word," : ",end="")                        # prints word : meaning   # end used for making word meaning in one line
        print(*meaning,sep=',')    # *is used for remove[],''  # prints all meanings of a same word with splitted in ,
                                    # * used for unpacking

def synonymn(myDict,synonymn_dict):     # defning synonymn fn with parameters
    if myDict=={}:                      # if myDict is empty return synoymn_dict
        return synonymn_dict
    else:
        key=[]                           # key as a list
        value=[]                         # value as a list
        for word,meaning in myDict.items():       # putting dictionary keys , values in word and meaning
            key.append(word)                     # appending word in key
            value.append(meaning)                # appending meaning in value 

        if value[0] not in synonymn_dict:          # if value's list 1st item is not in synonymn dictionary
            synonymn_dict[value[0]] = []            # synoymn dict 1st key's values list
            synonymn_dict[value[0]].append(key[0])      # appending words meaning
            myDict.pop(key[0])                           # then poping that word
        else:                                           # if value's list 1st item is in synonymn dictionary
            synonymn_dict[value[0]].append(key[0])      # then putting that value against key means where more values are putting
            myDict.pop(key[0])                        # then poping that word
        return synonymn(myDict,synonymn_dict)        # returning synoymn dictionary

main()                                               # calling main fn
