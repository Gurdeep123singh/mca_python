'''
program for checking if given expression i.e brackets is valid or not
i/p:- {(a+b)}
o/p:- valid
i/p:- {[}]
o/p:- not valid
'''
class parenthesis:
    top=-1
    def __init__(self,string,stack):       # constructor having stack and expression
        self.stack=stack
        self.expression=string
    
    def total_elements_in_stack(self):                     # giving tottal elements in stack
        return (len(self.stack))
    
    def push(self,i):                                      # push fn
        self.stack.append(i)
        parenthesis.top+=1                                 # incrementing top
    def pop(self):
        self.stack.pop()
        parenthesis.top-=1   
    def match(self):                                      # matching fn
        for i in self.expression:                         # expression goes in i one by one
            if i not in '[{()}]':
                pass
            elif i in '[{(':      
                self.push(i)                               # pusing element by calling fn
                
            elif i==')' and  self.total_elements_in_stack()!=0 and  self.stack[parenthesis.top]=='(' :  # if) and total elements in stack not=0 and top=(
                self.pop()
                
            elif i=='}' and self.total_elements_in_stack()!=0 and self.stack[parenthesis.top]=='{' : # if} and total elements in stack not=0 and top={
                self.pop()
                  
            elif i==']' and self.total_elements_in_stack()!=0 and self.stack[parenthesis.top]=='[': # if] and total elements in stack not=0 and top=[
                self.pop()
               
            else:    # if not then false ex if extra brace} or) or]
                return False
    def compare(self):
        if self.match()==False:            # if status false
            return False 
        if len(self.stack)==0:             # if stack is empty
            return True
          
        else:                               #if stack not empty
            return False

def main():
    obj=parenthesis(input(" enter expression : "),stack=[]) 
    status=obj.compare()
    if status==True:                                             # if status true
        print(" expression is valid ")
    else:                                                         # else false
        print("!!! expression is not valid !!!")    
if __name__=="__main__":
    main()            