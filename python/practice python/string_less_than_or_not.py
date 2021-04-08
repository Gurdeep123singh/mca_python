text = input("enter string")
length = len(text)
count=0
for i in text:
 if i ==' ':
     count=count+1
print(count)   
a= length-count
if (a)<10:
    print("yes less than 10")
else:
    print(a,"not less than 10")    