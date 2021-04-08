s = input("enter the string")
split1 =[] # empty array for list
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

length = 0
for word in split1:
 if (length<len(word)):
     length = len(word)
     word1 = word
print("length of largest word", length)    
print("the largest word is : ",word1) 