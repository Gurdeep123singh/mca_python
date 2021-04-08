s =input("enter string\n")
count = 0
triple = 0
for i in range(len(s)):
 if s[i] == ' ' and s[i+1] == ' ' and s[i+2] != ' ':
     count += 1
 if s[i] == ' ' and s[i+1] == ' ' and s[i+2] == ' ' and s[i+3] != ' ':   
     triple += 1 
print("double spaces are: ",count)      
print("triple spaces are: ",triple)


# or

double =0
triple =0
in_space =False
for i in range(len(s)):
    if s[i] == ' ' and s[i+1] == ' ' and not in_space:
       if s[i+2] ==' ':
           triple +=1
       else:
           double +=1
       in_space =True
    elif s[i] !=' ':
        in_space =False
print(double,triple)                 
