'''
program for calculating salary using classes and objects . you can describe how many employees you want to take
i/p :- name,EmpID,designation,experience
o/p :- name,EmpID,designation,experience and salary
'''
class employee:                                               # class
    count=0                                                    # count initialises as 0
    def __init__(self,name,EmpID,designation,experience):      # giving parametrs from users in main fn
        self.name=name
        self.EmpID=EmpID
        self.designation=designation
        self.experience=experience
    
  # getter

    def BaseSalary(self):                                           # using it for calculating base salary
        if self.designation=='worker':
            self.base=10000
        elif self.designation=='supervisor':
            self.base=15000 
        elif self.designation=='manager':
            self.base=20000          
        
    def AddSal(self):                                          # for calculating add salary
        self.BaseSalary()                                       # calling for having base salary
        self.Add=(self.experience/100)* (self.base)             
        
            


    def HRA(self):                                           # hra fn
        self.BaseSalary()                                    # calling base salary fn
        self.hra=(0.05 * (self.base))                        
        
        

    def Salary(self):                                      # for calculating salary 
        self.AddSal()                                      # calling
        self.HRA()
        self.BaseSalary()
        self.total=self.base + self.Add + self.hra            # adding
             
    def count1(self):                                        # counting of objects
        employee.count+=1                                      # +1
        return employee.count                                 # returning count value

    def set_values(self):                                                # setter
        print(f"\n\t\t\t enter details for employee {employee.count} : \n")   # for updating
        print("what you want to change: ")                     
        option=input("name(n) , id (i) or designation(d) or experience(e) or designation and experience(b) ").lower()
        if option=='n':
            self.name=input("enter name : ")
        elif option=="i":    
            self.EmpID=input("enter employee id : ")
        elif option=="d":  
            print('worker or supervisor or manager')
            self.designation=input("enter designation :   ").lower()  # making designation value as lower of input
        elif option=="e":    
            self.experience=float(input("enter experience in integer or float: "))  # taking expeience value as float
        elif option=="b":
            print('worker or supervisor or manager')
            self.designation=input("enter designation : ").lower() 
            self.experience=float(input("enter experience in integer or float : "))     
        else:
            print("wrong choice")
    def display(self):                                         # dispalying values
        
        
        print(f"if you want to change details for employee {employee.count1(self)}: ") # if want to change
        option=input('yes(y) or no(n) :').lower()
        if option=='y':
            employee.set_values(self)
        self.Salary()                                            # calling salary fn
        print(f" EMPLOYEE : {employee.count}")                       # printing employees details
        print(f"\n\t\t\t******* SALARY OF {self.name} ********")
        print(f"\n\t\t\tEMP_ID : {self.EmpID}")
        print(f"\t\t\tDESIGNATION : {self.designation}")
        
        print(f"\t\t\tEXPERIENCE : {self.experience}")
        print(f"\t\t\tSALARY : {self.total}")

    def __str__(self):                                     # printing employees details
        return '*****************  SALARY'+'\nNAME = '+self.name +'\nEmpID = ' + self.EmpID + '\nDesignation = ' + self.designation + '\nexperience = '+ str(self.experience) + '\nSalary = ' + str(self.total) + '\n**************************'
def main():        
    objects=int(input("HOW MANY employees YOU WANT TO take : "))      # asking for no of objects 

    employee_list = []                                          # objects list
    for i in range(objects):                                            # taking employees details
        print(f"\n\t\t\t enter details for employee {i+1} : \n")
        name=input("enter name : ")
        emp_id=input("enter employee id : ")
        designation_name=input("enter designation : \nworker or supervisor or manager : ").lower()
        experience=float(input("enter experience in integer of float: "))
        employee_list.append(employee(name,emp_id,designation_name,experience))    # making objects and append in objects list

    for i in range(objects):
        employee_list[i].display()                     # for displaying

        print("\t\t\t\tusing str\n")                              # using __str__
        print(employee_list[i].__str__())

main()                                                # calling main fn

