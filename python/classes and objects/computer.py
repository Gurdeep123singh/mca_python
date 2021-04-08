class computer:
    def _init_(self,colour,brand_name,processor_name,Ram_name):
        self.colour=colour
        self.brand_name=brand_name
        self.processor_name=processor_name
        self.Ram_name=Ram_name
    def color(self):
        print("the color of the computer is :",self.colour)

    def brand(self):
        print("the brand of the computer is :",self.brand_name)

    def processor(self):
        print("the processor of my computer is :",self.processor_name)

    def RAM(self):
        print("the ram of my computer is :",self.Ram_name)

s=computer()
# invoking object using self
colour=input("enter color of your computer : ")
# or computer.color(s) # or computer.color() without using object and space
brand_name=input("enter brand of your computer : ")
processor_name=input("enter processor of your computer : ")
Ram_name=input("enter ram of your computer : ")
s._init_(colour,brand_name,processor_name,Ram_name)
s.color()
s.brand()
s.processor()
s.RAM()