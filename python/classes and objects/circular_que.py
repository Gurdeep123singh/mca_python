class queue:
    def __init__(self,size):
        self.size=size
        self.list1=[]
        self.front=0
        self.rear=-1

    def enqueue(self,element):
        if self.front==0 and self.rear+1<self.size:
            
            self.rear+=1
            self.list1.insert(self.rear,element)
            print(self.rear)
            print(self.front)
        if(self.front==0 and self.rear+1==self.size) or self.rear+1==self.front :
            print(" NOW QUEUE is full ")
            
            print(self.rear)
            print(self.front)
        elif self.front!=0 and (self.rear-self.front)<self.size:  
            if self.rear==self.size:
                self.rear=0
            else:
                self.rear+=1
            self.list1.insert(self.rear,element)
            print(self.rear)
            print(self.front) 
            
    def dequeue(self):
        if (self.front==0 and self.rear==0) or (self.front==self.rear+1 and len(self.list1)==0) :
            print("empty queue")
            self.rear=-1
            self.front=0
            print(self.rear)
            print(self.front)

        elif self.rear<self.front and self.front<self.size:
            del self.list1[self.rear+1] 
            self.front+=1 
            print(self.rear)
            print(self.front)
        elif self.front==self.size:
            self.front=0
            del self.list1[self.front]
            self.front+=1 
            print(self.rear)
            print(self.front)
               
        else:
            del self.list1[0]
            self.front+=1
            print(self.rear)
            print(self.front)
            
            
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