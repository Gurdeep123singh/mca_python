
import pickle


def record(no,dict1,dict2,subject_name):
    print("enter student names :")

    name=[ input(f"enter student {i+1} name : ")  for i in range(no)]
    print(name)
    print("enter roll no for each student  :")

    roll=[ int(input(f"enter student {name[i]} roll no : ") ) for i in range(no)]
    print(roll)
    print("total no of subjects: ")
    number=int(input())

    subject_name=[input("enter subject name: ") for i in range(number)]


    print("enter marks")

    for i in range(no):
        print(f"enter marks for child  {name[i]} :") 
        dict2['roll no ']=roll[i]
        for j in range(number):
        
            dict2[subject_name[j]] = int(input(f"marks for {subject_name[j] } :  ") )
        dict1[name[i]] = dict2
    
    return dict1

def main():
    print("no of students: ")
    no=int(input())
    name=[]

    
    record_marks=record(no,dict1={},dict2={},subject_name=[]) 
    print("record of students",record_marks)  

    filename=input("enter filename : ")
    writing(filename,record_marks)
    reading(filename)


def writing(filename,content,mode='ab'):
    with open (filename,mode) as file:
        pickle.dump(content,file)

def reading(filename,mode='rb'):
    with open (filename,mode) as file:
        print(pickle.load(file))

main()   