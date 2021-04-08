class vector:                                                                          # class vector
    def __init__(self,vector1,vector2):                                                # vector1
        self.vector1=vector1                                                           # vector2
        self.vector2=vector2
    def sum(self):                                                                     # fn sum
        
        self.add=[self.vector1[i]+self.vector2[i] for i in range(len(self.vector1))]     # doing sum
        return self.add                                                                  # return sum
    def subtract(self):                                                                  # fn subtract
        self.minus=[self.vector1[i]-self.vector2[i] for i in range(len(self.vector1))]   # doing subtract
        return self.minus                                                                # return subtract
    def multiply(self):                                                                  # fn multiply
        self.into=[self.vector1[i]*self.vector2[i] for i in range(len(self.vector1))]    # doing multiply
        return self.into                                                                 # return multiply
def main():
    size=int(input("what is the size of vector :"))
    
    print("enter elements for vector 1")                                                # enter elements
    vector1=[int(input()) for i in range(size)]
    print("enter elements for vector 2")
    vector2=[int(input()) for i in range(size)]
    v=vector(vector1,vector2) 
    while True:                                                                       
        status = input("if you want to add(a) or subtraction(s) or multiply(m) or exit(e) :")
        if status=='a': 
            print("sum of two vectors :", v.sum())
        elif status=='s':    
            print("difference of two vectors is :",v.subtract())
        elif status=='m':
            print("multiplication of two vectors is :",v.multiply())
        elif status=='e':
            exit()    
        else:
            print("!!!!!INVALID OPTION!!!!!")
main()
