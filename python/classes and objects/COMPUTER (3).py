'''
program for having detils of ccomputers usiing class and objects . asking how many computers you want 
i/p:-colour,brand_name,processor_name,Ram_name
o/p:-colour,brand_name,processor_name,Ram_name and counting objects and comparing also that if laptops are same or different
'''
class computer:                                                 # computer class
    count=0                                                          # count initialises as 0
    def __init__(self,colour,brand_name,processor_name,Ram_name):     # having parameters from users through main fn
        self.colour=colour
        self.brand_name=brand_name
        self.processor_name=processor_name
        self.Ram_name=Ram_name
    def set_count(self):                          # for count of objects
        computer.count+=1
        return computer.count  

    # getter fn
         
    def color(self):                                             # having color                 
        return self.colour 
 
    def brand(self):                                          # having brand
        return self.brand_name 

    def processor(self):                                       # having processor value
        
        return self.processor_name

    def RAM(self):                                           # having ram value
        return self.Ram_name

    # setter fn    
    def set_color(self):                                        # setting colour
        self.colour=input("enter colour : ")
        return self.colour

    def set_brand(self):                                          # setting brand
        self.brand_name=input("enter brand : ")
        return self.brand_name

    def set_processor(self):                                       # setting processor
        self.processor_name=input("enter processor : ")
        return self.processor_name

    def set_RAM(self):                                          # setting ram
        self.Ram_name=input("enter ram : ")
        return self.Ram_name    

    def compare(self,v):                                       # comparing 2 objects 
        if self.colour==v.colour and self.brand_name==v.brand_name and self.processor_name==v.processor_name and self.Ram_name==v.Ram_name :
            print("objects are same") 
        else:
            print("objects are different")
    def display(self):                                         # for displaying
        print(f"IF YOU WANT TO CHANGE THE VALUES OF OBJECT :{computer.set_count(self)} \n yes(y) or no (n) : ")
        option=input()
        if option=='y':
            print("WHAT ATTRIBUTE YOU WANT TO CHANGE :")             # asking which attribute u have to update
            choice=input("color(c) or brand(b) or processor(p) or RAM(r) or all(a) :").lower()
            if choice=='c':
                computer.set_color(self)
            elif choice=='b':
                computer.set_brand(self)
            elif choice=='p':
                computer.set_processor(self)
            elif choice=='r':
                computer.set_RAM(self)
            elif choice=='a':
                computer.set_color(self)
                computer.set_brand(self)
                computer.set_processor(self)
                computer.set_RAM(self)
            else:                                    # if wrong option
                print(" WRONG CHOICE ")    
            

       
        print(f"\n\t\t\t object : {computer.count}\n")

        a=computer.color(self)                  # printing details of computers
        print(f" color is : {a}")
        b=computer.brand(self)
        print(f" brand is : {b}")
        c=computer.processor(self)
        print(f" processor is : {c}")
        d=computer.RAM(self)
        print(f" RAM is : {d}")
        
    def __str__(self):                                # using str fn for displaying
        return '**************** DETAILS'+'\ncolour = ' + self.colour + '\nbrand = ' +  self.brand_name+ '\nprocessor = ' + self.processor_name + '\nRAM = ' + self.Ram_name + '\n******************'    
            

                
def main():                                     # main fn
    objects=int(input("HOW MANY computers YOU WANT TO take : "))        # no of computers

    computer_list = []                                             # objects are appended in this list

    for i in range(objects):
        print(f"\n\t\t\t enter details for object{i+1} : \n")           # details of computer
        colour=input("enter color of your computer : ")
        brand_name=input("enter brand of your computer : ")
        processor_name=input("enter processor of your computer : ")
        Ram_name=input("enter ram of your computer : ")
        computer_list.append(computer(colour,brand_name,processor_name,Ram_name)) # making objects and then appending in list

    for i in range(objects):
        computer_list[i].display()         # for displaying
        print(" \t\t\t\tUSING STR \n")
        print(computer_list[i].__str__())         # calling str fn
    print("if you want to compare two models")           # for comparing 2 objects
    status=input("yes(y) or no(n) :").lower()
    if status=='y':
        if objects>1:
            print("if you want to compare two models")
            a=int(input("enter the computer no  :"))                                       # 1st object
            b=int(input("enter other computer no to compare with :"))                   # 2nd object
            if (a or b) < objects:                                        
                computer_list[a-1].compare(computer_list[b-1])
            else:                                                      
                print("  OUT OF RANGE ")    
        else:
            print("objects are less than 1 so cant able to compare")
main()                                                                    # calling main fn