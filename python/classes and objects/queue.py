class queue:
    def __init__(self,size):
        self.size=size
        self.list1=[]
        self.front=0
        self.rear=-1

    def enqueue(self,element):
        if (self.front==0 and self.rear+1==self.size) or (self.rear-self.front)+1==self.size:
            print(" QUEUE is full ")
        else:    
            self.list1.insert(self.rear+1,element)
            self.rear+=1 
            
    def dequeue(self):
        if (self.front==0 and self.rear==-1) or self.front==self.rear+1 or ( self.front==1 and self.rear==-1):
            print("empty queue")
            self.rear=-1
            self.front=0
        else:
            self.list1.pop(0)
            self.front+=1
            
            
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