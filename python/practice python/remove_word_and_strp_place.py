word=input("enter the word you want to remove")
def remove_word_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

string=" harry is a good boy "
n=remove_word_and_strip(string,word)    
print(n)