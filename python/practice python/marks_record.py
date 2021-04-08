'''
program to make record of students with roll no , subjects and their marks 
using fn and return and then printing record to user desired file
i/p :- taking no of students, subjects,marks
o/p:- {1: {'name': 'don', 'marks': {'oops': 20, 'csa': 30}}, 2: {'name': 'ron', 'marks': {'oops': 40, 'csa': 50}}}




'''
import pickle                                 # importing pickle


def enter_records(no):                         # fn records
    students = {}                            
    data = {}
    subject_name = {}

    print("enter student names :")                                            # entering students name
    name = [input(f"enter student {i+1} name : ") for i in range(no)]

    print("enter roll no for each student  :")                               # roll no entering and acts as key
    roll = [int(input(f"enter student {name[i]} roll no : "))
            for i in range(no)]
 
    
    print("total no of subjects: ")                             

    number = int(input())                                                  # taking no of subjects
    subject_name = [input("enter subject name: ") for i in range(number)]  # taking subjects name

    print("enter marks")                   # entering marks for individual students of each subjects
    for i in range(no):
        data[roll[i]] = {}                # creating roll no dictionary
        data[roll[i]]['name'] = name[i]              #data[rollno][name] has names       
        marks = {}
        print(f"Enter marks for child  {name[i]} :")
        for j in range(number):
            marks[subject_name[j]] = int(
                input(f"marks for {subject_name[j]}:  "))
        data[roll[i]]['marks'] = marks                    #data[rollno][name] has marks 

    return data                                          # returning records

            
def main():                                       # defining fn main
    print("no of students: ")
    no = int(input())
    name = []

    data = enter_records(no)
    print("record of students", data)                         # record of students

    filename = input("enter filename to save record data : ")    # filename           
    writing(filename, data)                                    # calling write fn to write
    reading(filename)


def writing(filename, content, mode='ab'):                        # writing content in file
    with open(filename, mode) as f:
        pickle.dump(content, f)


def reading(filename, mode='rb'):                        # reading for checking if data is written or not
    with open(filename, mode) as file:
        print(pickle.load(file))


main()                                                             # calling main fn
