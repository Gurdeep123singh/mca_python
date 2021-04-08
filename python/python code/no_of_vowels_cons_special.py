def vowels_constonant_special(s):
 c=0
 count=0      
 count1 = 0 
 count2 = 0
 list1 = ["a","e","i","o","u"]  # list of vowels
 list2 = [0,1,2,3,4,5,6,7,8,9]   # list of 0 to 9
 length = len(s) # taking length
 for i in s:
   if(i == " " ):  # if space then another word start
      count = count + 1 # +1 for counting last one also
   print("length of string",length-count) # length of original string - spaces 
 for i in s:
     if i in list1:   # if vowels are in list
         count1 = count1 + 1   # makes count+1
     elif(i>'a' and i<='z') :  # otherwise consonants
         count2 = count2 + 1   # makes count+1
     elif(i!=list1 and i!=list2 and i!=" "):  # otherwise not vowels not consonants and not no.'s and not space
         c= c+1      # for special character
 print("no of vowels are: ", count1)
 print("no. of consonants are: ", count2)

     

 print("no. of special characters  are: ", c)

def main():
 s = input(" enter the string")
 s = s.lower()   # making upper input to low so we compare only lower no need of upper     
 vowels_constonant_special(s)

main()