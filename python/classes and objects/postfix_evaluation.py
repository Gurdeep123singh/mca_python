'''
program to evaluate postfix expression by using stack
it takes expresion in form of variable and then ask for value of variables 
i/p:= ab+
a=2
b=3
o/p:- 5
'''
class postfix:
    
    def __init__(self,string,stack):   # constructor
        self.expression=string
        self.stack=stack
        self.top=-1
        self.dict1=dict()       #  making dictionary for putting the values of variable for expression
        
    def push(self,i):
        self.stack.append(i)                 # appending elements
        self.top+=1                          # incrementing pointer
    def pop(self):
        self.stack.pop()               
        self.top-=1
    def solve(self):                                    # solving postfix
        for i in self.expression:                       
            if 'a'<=i<='z' :                          # if i is  a to z
                if i not in self.dict1:                    # then if not in dict by taking value of variable it gets added into dictionary and 
                    no=int(input(f'what is the value of {i}:'))    # pushing into stack    
                    self.dict1[i]=no
                    self.push(no)
                else:                                     # else  only appending into stack
                    self.push(self.dict1[i])
            elif i in '+*/-%#^' and len(self.stack)>1:                           # evaluation takes place
                if i=='+': c=(self.stack[self.top-1] + self.stack[self.top])
                elif i=='*': c=(self.stack[self.top-1] * self.stack[self.top])
                elif i=='/': c=(self.stack[self.top-1] / self.stack[self.top])
                elif i=='-': c=(self.stack[self.top-1] - self.stack[self.top])
                elif i=='%': c=(self.stack[self.top-1] % self.stack[self.top])
                elif i=='#': c=(self.stack[self.top-1] // self.stack[self.top])
                elif i=='^': c=(self.stack[self.top-1] ** self.stack[self.top])
                self.pop()                        # when operation had been takes place between 2 variables then that variables re poped out
                self.pop()   
                      
                self.push(c)                    # result stored into stack for further operation
                
               
        return self.stack                      # returning stack

def main():
    print(" FOR REMAINDER(%) , DIVIDE IN FLOAT(/), DIVIDE IN INTEGER(#) , EXPONENT(^)")
    string=input(" Enter expression in variable: ")
    obj=postfix(string,stack=[])                                                             # making object of class 
    ans=obj.solve()                                                                         # calling fn of obj class
    print(" Solving expression output is : ", *ans)        
main()    