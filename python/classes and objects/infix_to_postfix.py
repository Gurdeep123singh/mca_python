'''
program for conversion from infix to postfix
and for checking exprssion is having proper brackets or not so use import class parenthesis class from 
all_parenthesis filename
'''
from all_parenthesis import parenthesis

class conversion:
    def __init__(self,string,stack): # constructor
        self.expression=string
        self.stack=stack
        self.top=0                     # top pointr=0
       
        
        
        
    def push(self,i):              # pushing elements in stack
        
        self.stack.append(i)
        self.top+=1
    
    
    

    def infixToPostfix(self,stk):
        # dict contain Precedence order
        pre={'{':1,  '}':1,  '[':1,  ']':1,  '(':1,  ')':1,
        '+':2,  '-':2,  '*':3,  '/':3,  '%':3, '@':3, '^':4
        }
        #iterating in expression
        for i in self.expression:
            # when i is number or char add it to stack
            if i.isalpha():
                self.push(i)
            # when i is opening bracket add it to stk
            elif i=='(' or i=='[' or i=='{':
                stk.append(i)
            # when i is closing bracket
            elif i==')' or i==']' or i=='}':
                # pop element from stk
                topElement=stk.pop()
                # asign bracket for while loop
                if i==')': bracket='('
                elif i==']': bracket='['
                elif i=='}': bracket='{'

                # while loop to add  operator to stack
                while topElement!=bracket:
                    self.push(topElement)
                    topElement=stk.pop()
            else:
                #loop for adding operator to stack from stk
                while (not len(stk)==0) and (pre[stk[-1]] >= pre[i]):
                    self.push(stk.pop())
                #push operator to stack
                stk.append(i)
        #loop to add remain operator to stk
        while not len(stk)==0:
            self.push(stk.pop())
        
        return self.stack
        
def main():
    print(" FOR REMAINDER(%) , DIVIDE IN FLOAT(/), DIVIDE IN INTEGER(#) , EXPONENT(^)")
    string=input("enter expression : ")
    import_obj=parenthesis(string,stack=[])                         # making object of import class
    status=import_obj.compare()                                    # calling import class fn to check if expression is valid or not
    if status==True:                                             # if status true then gives expression valid and convert infix to posfix
        print(" expression is valid ")
        obj=conversion(string,stack=[])
        list1=obj.infixToPostfix(stk=[])
    
        new_exp=''                                                       # conversion of list items into string
        for i in list1:
            new_exp+=i
        print(" postfix expression : ",new_exp)
    else:                                                         # else false
        print("!!! expression is not valid !!!")

    
main()    