class computer:
    count=0
    def _init_(self,colour,brand_name,processor_name,Ram_name):
        self.colour=colour
        self.brand_name=brand_name
        self.processor_name=processor_name
        self.Ram_name=Ram_name
    def set_count(self):
        computer.count+=1
        return computer.count   
    def color(self):
        return self.colour

    def brand(self):
        return self.brand_name

    def processor(self):
        return self.processor_name

    def RAM(self):
        return self.Ram_name

    def compare(self,v):
        if self.colour==v.colour and self.brand_name==v.brand_name and self.processor_name==v.processor_name and self.Ram_name==v.Ram_name :
            print("objects are same") 
        else:
            print("objects are different")
    def display(self):
        # object 1
        print("the object :",computer.set_count(self))

        a=computer.color(self)
        print(f"the color is : {a}")
        b=computer.brand(self)
        print(f"the brand is : {b}")
        c=computer.processor(self)
        print(f"the processor is : {c}")
        d=computer.RAM(self)
        print(f"the RAM is : {d}")


s=computer()
v=computer()
# invoking object using self
colour=input("enter color of your computer : ")
# or computer.color(s) # or computer.color() without using object and space
brand_name=input("enter brand of your computer : ")
processor_name=input("enter processor of your computer : ")
Ram_name=input("enter ram of your computer : ")
s._init_(colour,brand_name,processor_name,Ram_name)
s.display()





v._init_(colour,brand_name,processor_name,Ram_name)
colour=input("enter color of your computer : ")
# or computer.color(s) # or computer.color() without using object and space
brand_name=input("enter brand of your computer : ")
processor_name=input("enter processor of your computer : ")
Ram_name=input("enter ram of your computer : ")
v.display()

s.compare(v)