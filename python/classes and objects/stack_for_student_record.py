'''
program for students record in stack using 2 classes having pop ,push ,total elements ,peek and display operations
using top pointer , list . It is taking students name , roll no as a students record
i/p:- asking for size of stack
then which operation to perform
o/p:- giving answers according to the operations
'''
class student:                                           # class student
    #constructor
    def __init__(self,studentName,studentRollNo):
        self.name=studentName                            # taking name
        self.rollNo=studentRollNo                        # taking roll no

    #defining __str__()
    def __str__(self):
        return ' Name: '+self.name+' Roll NO: '+str(self.rollNo)
    def __repr__(self):                                       # defining repr for not giving reference of objects
        return self.__str__()                        # returning __str__ return

class stack:                                         # class stack
    top=-1                                           # top is initialised as -1
    def __init__(self,elements,size):                # constructor
        self.elements=elements                       # elements list
        self.size=size                               # size of element list
        
    def push(self,stu):                              # parameter student object
        if (stack.top +1 )==self.size:               # if stack's top pointer== size then returns false
            return False
        else:                                        # else appends
            
            self.elements.append(stu)              
            stack.top+=1                             # and increment pointer when appends
            return self.elements                  
        
    def pop(self):                                   # for pop
        if stack.top==-1:                            # this means stack is empty as top=-1
            return False
        else:                                        # if not emptied then pop the element
            self.poped_element=self.elements[-1]     # poped element is first stored before doing pop
            self.elements.pop(-1)                    # doing pop   
            stack.top-=1                             # decrementipng top pointer with -1
            print(f"\t\t\t\t POPPED ELEMENT IS : {self.poped_element}")    # showing poped element

    def total_elements_in_stack(self):                      # giving tottal elements in stack
        return (stack.top+1)                                # returning

    def peek(self):                                   # peeking top element in the sack
        if stack.top==-1:                             # if top=-1 means empty stack; returning none
            return None
        else:                                    
            return self.elements[-1]                  # else returning element on top 
    def show(self):                                   # displaying elements in the stack
        return self.elements 


def main():                                           # main fn
    
    
    elements=[]                                                    # list
    size=int(input("What is the size of your stack : "))           # taking size
    # len(elements)<=size
        
    obj=stack(elements,size)                                       # making object of stack
    while True:
        flag=input("\t\t\t\twhat you want to do \n \t\t\tpush(1) or pop(2) or no_of_elements in stack(3) \nor peek top element(4) or show(5) or exit(6) : ")
        if flag=='1':
            studentName=input('Enter student name = ')
            studentRollNo=int(input('Enter the Roll NO. = '))
            stu=student(studentName,studentRollNo)                     # making student object
            status=obj.push(stu)
            if status==False:                                          # if status false means full stack
                print(" \t\t\t\t!!!!!! STACK IS FULL !!!!!! ")
            else:  
                print(f'\t\t\t\tpushing operation is done ->>>> {stu} ')  # telling push is this and done
        elif flag=='2':
            status1=obj.pop()
            if status1==False:                                                   # if false emptied stack
                print("\t\t\t\t!!!!!!!! STACK IS EMPTY !!!!!!!!")
            else:    
                print(f'\t\t\t\tpoping operation is done ->>>> ')      # telling poping is done
        elif flag=='3':
            print(f" \t\t\t\tNO. OF ELEMENTS ARE IN STACK IS : {obj.total_elements_in_stack()}")  # total elements in stack
        elif flag=='4':
            print(f"\t\t\t TOP ELEMENT IN THE STACK IS : {obj.peek()}")       # top element of stack 
        elif flag=='5':
            print(f"your stack is : {obj.show()}")           # displaying stack
        elif flag=='6':
            exit()                                          # for exit
        else:
            print('!!!! INVALID OPTION !!!!')
main()                                                  # calling main fn
