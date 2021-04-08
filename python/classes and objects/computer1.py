class computer:
    def _init_(self,colour,brand_name,processor_name,Ram_name):
        self.colour=colour
        self.brand_name=brand_name
        self.processor_name=processor_name
        self.Ram_name=Ram_name
    def color(self):
        return self.colour

    def brand(self):
        return self.brand_name

    def processor(self):
        return self.processor_name

    def RAM(self):
        return self.Ram_name

s=computer()
# invoking object using self
colour=input("enter color of your computer : ")
# or computer.color(s) # or computer.color() without using object and space
brand_name=input("enter brand of your computer : ")
processor_name=input("enter processor of your computer : ")
Ram_name=input("enter ram of your computer : ")
s._init_(colour,brand_name,processor_name,Ram_name)
a=s.color()
print(f"the color is : {a}")
b=s.brand()
print(f"the brand is : {b}")
c=s.processor()
print(f"the processor is : {c}")
d=s.RAM()
print(f"the RAM is : {d}")