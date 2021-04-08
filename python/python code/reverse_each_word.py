# doesn't treturns value
def reverse_each_word(s):
 split1 =[] # empty  array for list
 temp ='' # for putting names in ''
 for c in s:
     if c == ' ':   # if space in string 
         split1.append(temp)    # then array is append with ''
         temp =''
     else:
         temp += c   # '' is concatening with string 
 if temp:
     split1.append(temp)            # putting string into []
 print(split1)   # giving list 
 reverse = []  # empty 
 for i in split1:
     reverse.append(i[::-1])   # -1 for reversing and putting into [] 
     
 sentence = " ".join(reverse) # making it into string from list
 print("reverse word is : ",sentence)

def main():
    s = input("enter the string\n")
    reverse_each_word(s)  #  calling value function
main()     # calling main