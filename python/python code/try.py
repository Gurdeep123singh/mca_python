## template for a company and replacing name and date
name = input("Enter your name\n")
date=input("enter date\n")
letter = ''' Dear , <|NAME|>
You are selected!
date : <|DATE|>
'''
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)

# detecting double spaces in a string

s = input("enter a string")
flag = 0
if (s=="  "):
   flag=flag+1 
print("no of double space is :", flag)   