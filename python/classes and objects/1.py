class queue:    
    def __init__(self,size):  
        self.size=size
        self.list1=[]
        self.front=0
        self.rear=-1

    def enqueue(self,element): 
        if ((self.rear+1==self.size) and self.front==0) or ((self.front-1==self.rear) and len(self.list1)==self.size) or ((self.front==self.rear-1) and len(self.list1)==self.size):
            
            if ((self.rear+1==self.size) and self.front==0):
                self.rear=-1
                self.front=0
            print("full queue") 
        elif self.front<=self.rear:
            if self.rear==self.size:
                self.rear=0
                self.list1.insert(self.rear,element)
                self.rear+=1
            else: 
                self.rear+=1  
                self.list1.insert(self.rear,element)
                
        elif self.front>self.rear:
            if self.front==self.size:
                self.front=0
            self.rear+=1    
            self.list1.insert(self.rear,element)
                            
        else:
            self.rear+=1
            self.list1.insert(self.rear,element)    
    def dequeue(self):
        if (self.rear==-1 and len(self.list1)==0) or ((self.front==(self.rear-1)) and len(self.list1)==0) or (((self.front)==self.rear+1) and len(self.list1)==0):
            if (self.front==self.rear-1 and len(self.list1)==0):
                self.rear=-1
                self.front=0
            print("empty queue")
        elif self.front<=self.rear :
            
            del self.list1[self.front]
            self.front+1 
        elif self.rear<self.front   :
            if self.front!=self.size:
                pass 
            else:
                self.front=0
            del self.list1[self.front]
            self.front+1


    def display(self):
            
        print(self.list1)                                       



def main():
    size=int(input("what is the size of queue"))
    obj=queue(size)

    while True:
        print("WAHT YOU WANT TO DO ")
        option=int(input("ENQUEUE(1) DEQUEUE(2) DISPLAY(3) OR EXIT(0)"))
        if option==1:
            obj.enqueue(input('enter element to enqueue'))
        elif option==2:
            obj.dequeue()    
        elif option==3:
            obj.display()
        elif option==0:
            exit()
        else:
            print("!!!!!INVALID OPTION!!!!!")            
main()    