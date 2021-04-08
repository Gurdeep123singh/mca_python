# doesnt returns value
def largest(input1):   # making function
 a=[]
                            #first takes maximum length
 
 input1 = input1.split()
 for i in input1 :    # input values into i
     a.append(len(i))     # length values is appended into empty
 maximum = max(a)        # taking maximum length from a list of length

 print("largest word is : ")
 for i in input1 :
     if len(i)==maximum :     # comparing maximum value with input length and if it equals then it prints
         print(i)    # print word of maximum length


def main():
  input1 = input("enter string\n")     
  largest(input1) # calling function
main()