s =input("enter the string")
def biggest_word(s):
    in_word = False
    start = 0
    largest = ''
    for i in range(len(s)):
        if s[i] in (' ','\n ',' \t' ) and in_word:
            if len(s[start:i]) > len(largest):
                largest=s[start:i]
            in_word = False
        elif in_word == False:
            start = i
            in_word = True
    if in_word and len(s[start:]) > len(largest):
        largest = s[start:]
    return largest                    
print(biggest_word(s))    