'''Queue class 
   Variables:
            --> rear                    initially -1
            --> front                   initially -1
            --> size                    to store size of queue
   Functions:
            --> __init__                    constuctor
            --> enqueue                     to add element in circular queue
            --> dequeue                     to remove element in circular queue
            --> total_elements              to return total number of element in simple queue
            --> display                     to display queue
'''
class cq:
    def __init__(self, size): # constructor
        self.size = size
        self.queue = [None for i in range(size)]     # initialise queue with none
        self.front = self.rear = -1
        self.size1=0

    def enqueue(self, element):
        if ((self.rear + 1) % self.size == self.front):  # if queue is full
            return None

        elif (self.front == -1):    # if queue is empty then make front and rear=0 
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = element  # then putting the element in rear
            self.size1+=1
        else:            
            self.rear = (self.rear + 1) % self.size      # for putting elements for next rear
            self.queue[self.rear] = element
            self.size1+=1
            
        return element
    def dequeue(self):
        if (self.front == -1):                               #  for empty queue
            return None                                           
        elif (self.front == self.rear):                 # for only one element in queue
            poped_element=self.queue[self.front]         # putting that elemnt in POPED_ELEMENT
            self.queue[self.front] =None
            self.front = -1                             #  making rear and front again -1
            self.rear = -1 
            self.size1-=1           
        else:                                         # if elements are there in queue
            poped_element = self.queue[self.front]   # putting that elemnt in POPED_ELEMENT
            self.queue[self.front] =None
            self.front = (self.front + 1) % self.size   # changing front
            self.size1-=1             
        return poped_element                        # returning that poped element

  

    def display(self,opt):                              # display
        if opt==1:
            return self.queue
        else:
            s=''
            if(self.front == -1): 
                return None

            else:
                for i in range(self.size1) :
                    s=s+' '+self.queue[(self.front+i)%self.size1]
                return s                      

            

    def total_elements(self):                       # total_elements
        count=0
        for i in self.queue:                        
            if i!=None:
                count+=1
        return count        
def main():
    size=int(input("what is the size of queue : "))
    obj=cq(size)

    while True:
        print("WHAT YOU WANT TO DO ")
        option=int(input("ENQUEUE(1) DEQUEUE(2) DISPLAY(3) OR TOTAL ELEMENTS(4) EXIT(0)"))
        if option==1:                                                                 # for enqueue
            
            status=obj.enqueue(input('enter element to enqueue'))
            if status==None:
                print('QUEUE IS FULL')
            else:
                print('ENQUEUED ELEMENT ->>>',status)    
        elif option==2:                                            # for deque
            status1=obj.dequeue()
            if status1==None:
                print('QUEUE IS EMPTY')
            else:

                print("the element is dequed from queue->>",status1 )   
        elif option==3: 
            while True:                                                           # for display
                print("want to see list or only elements in the queue:")
                opt=int(input('FOR LIST(1) or ELEMENTS(2)'))
                if opt==1 or opt==2: break
                else: print("\t\tInvalid option!! Enter Valid Option")
            stat=obj.display(opt)
            if opt==1:
                print(stat)
            else:
                
                if stat==None:
                    print('empty queue')                         
                    
                else:
                    print("elements are->>>",end = " ")                      # end for in one line
                    print(stat,end='')                                       # end for in  one line
                    print()                                                  # for new line 
                 
        elif option==4:                                                           # for total elements
            print('TOTAL ELEMENTS IN QUEUE IS ->>',obj.total_elements()   ) 
        elif option==0:
            exit()
        else:
            print("!!!!! INVALID OPTION !!!!!")            
main() 
  