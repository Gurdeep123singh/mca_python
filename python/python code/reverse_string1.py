def reverse(s):
 str_1 = ""  # to store reverse string in empty string
 for i in s: 
   str_1 = i + str_1 # acts as a stack
 return str_1

s = input("enter the string to reverse")

print("the reverse string is :", reverse(s))  