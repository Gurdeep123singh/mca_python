class parenthesis_match:
    top=-1
    count_open_brace=0
    count_closed_brace=0
    def __init__(self,string,stack):
        self.expression=string
        self.stack=stack

    def match(self):
        for i in self.expression:
            if i=="(" :
                self.stack.append(i)
                parenthesis_match.top+=1
            elif i==')' and parenthesis_match.top>-1:
                self.stack.pop(-1)
                parenthesis_match.top-=1
            elif i==')' and parenthesis_match.top==-1:
                parenthesis_match.count_open_brace +=1
                

    def compare(self):
        self.match()
        if parenthesis_match.top==-1 and parenthesis_match.count_open_brace ==0:
            return True
        else:
            return False     
    
    def missing(self):
        if parenthesis_match.count_open_brace>0:
            print(f"{parenthesis_match.count_open_brace} open brace is missing ")
        elif parenthesis_match.top>-1:
            print(f" {(parenthesis_match.top)+1} close brace is missing ")     
def main():
    string=input(" type the expression:")    
    obj=parenthesis_match(string,stack=[])
    status=obj.compare()
    if status==False:
        print(" PARENTHESIS MISSING IN THE EXPRESSION ")
    else:
        print(' ALL PERFECT ')
    obj.missing()        
main()                    