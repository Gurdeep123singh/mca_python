# doesnt returns
# count no of words 
def count(s):  # defining functions
 count =0 


 for i in s:
   if(i == " " ):  # if space then increment count
      count = count + 1  # incrementing count
 print("no. of words in a strings are :  ",count+1)  # +1 becoz for end word
  

 # count no of letters 

 print("no. of letters in a string : ",(len(s)-count))  # length of original string - space gives no of letters

def main(): # defining main for calling count function 
  s =input("enter string")
  count(s) # calling function count
main()  # calling main