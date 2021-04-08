class stack:
    top=-1
    def __init__(self,elements,size):
        self.elements=elements
        self.size=size
        
    def push(self):
        if (stack.top +1 )==self.size:
            return False
        else:
            
            self.elements.append(int(input(" Tell the element to push")))
            stack.top+=1
            return self.elements
        
    def pop(self):
        if stack.top==-1:
            return False
        else:
            self.poped_element=self.elements[-1]
            self.elements.pop(-1)
            stack.top-=1
            print(f"\t\t\t\t POPPED ELEMENT IS : {self.poped_element}")   
    def show(self):
        return self.elements

    def total_elements_in_stack(self):
        return (stack.top+1)   

    def peek(self):
        if stack.top==-1:
            return None
        else:
            return self.elements[-1]    

def main():
    
    elements=[]
    size=int(input("What is the size of your stack : "))
    # len(elements)<=size
    obj=stack(elements,size)
    while True:
        flag=int(input("\t\t\t\twhat you want to do \n \t\t\tpush(1) or pop(2) or show(3) or no_of_elements in stack(4) \nor peek top element(5) or exit(6) : "))
        if flag==1:
            status=obj.push()
            if status==False:
                print(" \t\t\t\t!!!!!! STACK IS FULL !!!!!! ")
            else:  
                  
                print(f'\t\t\t\tpushing operation is done ->>>> ')
        elif flag==2:
            status1=obj.pop()
            if status1==False:
                print("\t\t\t\t!!!!!!!! STACK IS EMPTY !!!!!!!!")
            else:    
                print(f'\t\t\t\tpoping operation is done ->>>>')
                
        elif flag==3:
            print(f'\t\t\t\t STACK  IS : {obj.show()}')
        elif flag==4:
            print(f" \t\t\t\tNO. OF ELEMENTS ARE IN STACK IS : {obj.total_elements_in_stack()}") 
        elif flag==5:
            print(f"\t\t\t TOP ELEMENT IN THE STACK IS :{obj.peek()}")        
        elif flag==6:
            exit()           
main()
