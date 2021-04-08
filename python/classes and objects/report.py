class Report:
    count=0
    def __init__(self,name,course,marks_tuple,total_marks):
        self.name=name
        self.course=course
        self.marks_tuple=marks_tuple
        self.total_marks=total_marks
    def percentage(self):
        sum=0
        for i in range(len(self.marks_tuple)):
            sum+=self.marks_tuple[i]
        percentage=int((sum/self.total_marks)*100)
        return percentage    

    def grade(self):
        percen=self.percentage
        if percen > 90:
            return 'A+'
        elif percen > 75:
            return 'A'
        elif percen > 60:
            return 'B+'
        elif percen > 50:
            return 'B'
        elif percen > 40:
            return 'C'    
        else:
            return 'FAIL'    


    def set_count(self):
        Report.count+=1
        
        return Report.count

        

        
    
    def display(self):
        print(f"########### count = {Report.set_count(self)}")
        print(f"******* REPORT OF {self.name}********")
        print(f"class : {self.course}")
        print(f"MARKS : {self.marks_tuple}")
        print(f"Percentage : {Report.percentage(self)}")
        print(f"GRADE : {Report.grade(self)}")
        

Report("gurdeep","MCA",(10,30,40,50),500).display()


