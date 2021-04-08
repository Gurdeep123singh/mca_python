import matplotlib.pyplot as plt 

class Student:                                  # students records
       
    def __init__(self, name, markslist):        # constructor
        self.set_Name(name)                            # name will go in set_name fn
        self.set_MarkList(markslist)                   # marks list of individual student
        self.set_Percentage()                          # making %
        self.set_Grade()                               #  setting grades
    
        
    def set_Name(self,name):                    # setter 
        self.name=name    
    def set_MarkList(self,markslist):
        self.markslist=markslist  
    def set_Grade(self):                        # setting grades of a student
        
        if self.percentage>90:
            self.grade='A+'
        elif self.percentage>75:
            self.grade='A'
        elif self.percentage>60:
            self.grade='B'
        elif self.percentage>50:
            self.grade='C'
        elif self.percentage>40:
            self.grade='D'
        else:
            self.grade='Fail'  

    def set_Percentage(self):
        total_marks=len(self.markslist)*100
        self.percentage=(sum(self.markslist)/(total_marks))*100
        
    
    def get_Name(self):                        # getter for name it has name from set_name and then it returns
        return self.name
    def get_MarkList(self):                   # getter for markslist it has name from set_markslist and then it returns
        return self.markslist
    def get_Grade(self):
        return self.grade
    def get_Percentage(self):
        return self.percentage

def extract_data(stu_List,subjects_list):
    
    subj_marks=[[] for i in range(len(subjects_list))]
    names=[]
    max_marks_subj=[]
    perc=[]
    grades=[]
    for i in stu_List:                                    # list of students
        names.append(i.get_Name())                       # appending name in name list
        perc.append(i.get_Percentage())
        grades.append(i.get_Grade())
        m=i.get_MarkList()                         # taking markslist of individual student
        index=0                                   # for making index
        for j in m:
            subj_marks[k].append(j)         # making marks list for individual subjects for students
            index+=1
            
    for s in subj_marks:                     # going individual subjects marks list
        max_marks_subj.append(max(s))        # containing max marks of each subject
        
    return names,subj_marks,max_marks_subj,perc,grades     # returning all maked values
     
def choice1(self):            
    x = self.names
    y = self.perc
    plt.bar(x,y)
    plt.xlabel("Name of Students")
    plt.ylabel("Percentage of Students.")
    plt.show()
    
def choice2(self,stu_List,subjects_list,names_list): 
    s_name = input("\nEnter the name of student who u want pie chart analysis : ")
    
    if s_name in names_list:
        for i in stu_List:
            if s_name==i.get_Name():
                xpoints = subjects_list
                ypoints = i.get_MarkList()
                plt.pie(ypoints,labels = xpoints)
                plt.title("Result of "+s_name)
                plt.show()    
    else:
        print("\nNo user found.")
        
def choice3(names,grades):            
    x = names
    y = grades
    plt.plot(x,y,'o:r')
    plt.xlabel("Students")
    plt.ylabel("Grades")
    plt.show()
    
def choice4(grades):
    gr_list=['A+','A','B','C','D','Fail']
    a1=a2=b1=b2=c=f=0
    for i in grades:
        if i=='A+':
            a1=a1+1
        elif i=='A':
            a2=a2+1
        elif i=='B':
            b1=b1+1
        elif i=='C':
            b2=b2+1
        elif i=='D':
            c=c+1
        else:
            f=f+1
    gr_count=[a1,a2,b1,b2,c,f]
    x = gr_list
    y = gr_count
    plt.bar(x,y)
    plt.xlabel("Grades")
    plt.ylabel("Grades Count")
    plt.show()

def choice5(names,subj_marks,subjects_list):
    print("\nChoose a subject from : ")
    j=1
    for i in subjects_list:
        print(j,"-",i,".")
        j=j+1
    c=int(input("Enter ur choice for subject : "))
    if c>0 and c<=5:
        x = names
        y = subj_marks[c-1]
        plt.bar(x,y,width=0.1,color='red')
        plt.xlabel("Names")
        y_label="Marks in "+subjects_list[c-1]
        plt.ylabel(y_label)
        plt.show()
    else :
        print("Wrong Choice selected !!!")
        
def choice6(max_marks_subj,subjects_list):
    x = subjects_list
    y = max_marks_subj
    plt.bar(x,y)
    plt.xlabel("Subjects")
    plt.ylabel("Maximum marks in each subject")
    plt.show()
    
def choice7(stu_List,subjects_list,names_list): 
    s_name = input("\nEnter the name of student for who u want bar graph analysis : ")
    
    if s_name in names_list:
        for i in stu_List:
            if s_name==i.get_Name():
                xpoints = subjects_list#on x axis
                ypoints=i.get_MarkList()
                plt.bar(xpoints,ypoints)#plotting
                plt.xlabel("Subjects")
                y_label="Marks of "+ s_name
                plt.ylabel(y_label)
                plt.show()#for graph to get visible   
    else:
        print("\nNo user found.")    
   
#Defining main function. 
def main():
    #Maximum marks for each subject is 100.
    

    stu_List=[Student('a',[67,49,57,45,56]),Student('b',[68,75,89,99,91]),Student('c',[96,98,90,85,89]),Student('d',[78,56,43,86,93])]
    subjects_list = ['Maths','Eng','Hindi','SSt','Science']
    
    print(stu_List)
    names_list,subj_marks,max_marks_subj,perc,grades = extract_data(stu_List,subjects_list)
    
    
    while True:#begin while loop
        #printing menu options
        print("\n***** Menu *****")
        print("1-Percentage of all Students.")
        print("2-Pie chart analysis for Individual Student.")
        print("3-Grades of all Students.")
        print("4-Grades Count over all students.")
        print("5-Analysis subject wise.")
        print("6-Subject wise maximum marks.")
        print("7-Bar Graph analysis for Individual Student.")
        c=int(input("\nEnter your choice : "))
        #exceuting according to choice entered by user
        if c==1:
            choice1(names_list,perc)
        elif c==2:
            choice2(stu_List,subjects_list,names_list)
        elif c==3:
            choice3(names_list,grades)
        elif c==4:
            choice4(grades)
        elif c==5:
            choice5(names_list,subj_marks,subjects_list)
        elif c==6:
            choice6(max_marks_subj,subjects_list)
        elif c==7:
            choice7(stu_List,subjects_list,names_list)
        else:
            print("\nWrong choice Entered !!!")
        ch=input("\nDo u Want to continue? (Y/N) : ") #Input for while loop continuation till required.

# Calling main function
main()