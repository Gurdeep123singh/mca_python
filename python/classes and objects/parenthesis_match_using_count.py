class parenthesis:
    count=0
    count1=0
    def __init__(self,string):
        self.expression=string

    def match(self):
        for i in self.expression:
            if i=="(":
                parenthesis.count+=1
            elif i==')':
                parenthesis.count1+=1  

    def compare(self):
        self.match()
        if parenthesis.count==parenthesis.count1:
            return True
        else:
            return False                


def main():
    string=input(" type the expression:")    
    obj=parenthesis(string)
    status=obj.compare()
    if status==False:
        print(" PARENTHESIS MISSING IN THE EXPRESSION ")
    else:
        print(' ALL PERFECT ')    
main()        