def main():
  n = int(input("enter marks for which you want to have grade"))
  grade(n)


def grade(n):
  
  if (n>=90):
    print("grade is A+")

  elif (n>=80 and n<90):
    print("grade is A")

  elif (n>=70 and n<80):
    print("grade is B+")
  
  elif (n>=50 and n<70):
    print("grade is B")

  elif (n<50):
    print("grade is C")

  else:
   print("improve your numbers")      
main()        

    
