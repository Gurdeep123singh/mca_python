'''
this program is making marksheets and highest scorers txt file
program for making marksheet for all names and making their marksheets . txt files by reading binary file of 
record marks and then also making highest scorees marks in subject and names also in highest.txt file
by using functions

'''
import pickle


def main():
    filename = input("enter file name: ")
    file_of_marks = open(filename, 'rb')                    # openinf file read binary
    data = pickle.load(file_of_marks)                          # load in data

    for roll, entry in data.items():                                                # for each student
        fileName = entry['name'] + '_' + str(roll) + '.txt'
        marks = entry['marks']                         # marks
        Marksheet(fileName, entry['name'], roll, marks)
        print('the creation of ', fileName, 'is done')

    HighestScorers(data)                                # calling highest scores
    file_of_marks.close()  # close


def Marksheet(fileName, name, rollno, marks, mode='wt'):        # marksheet for each student

    with open(fileName, mode) as markSheet:                          # open the file
        markSheet.write('\t\t    Marks Sheet   \n\t  Name:')
        markSheet.write(name)
        markSheet.write('\t   Roll No.:')
        markSheet.write(str(rollno))
        markSheet.write('\n\t------Marks-----\n')
        markSheet.write('\tSubject\t\tMarks\n')
        for (subject, m) in marks.items():
            markSheet.write('\t')                            # space
                                                           # subject name
            markSheet.write(subject)
            markSheet.write('\t\t')                       # space
                                                      # marks for each subject
            markSheet.write(str(m))
            markSheet.write('\t\t')
            markSheet.write('\n')


def HighestScorers(data):            # fn for highest marks
    highest = {}
    for roll, entry in data.items():              # taking roll no and names
        for sub, num in entry['marks'].items():
            if highest.get(sub) == None:              # comparing
                highest[sub] = (roll, num)
            elif highest[sub][1] < num:
                highest[sub] = (roll, num)

    with open('highest.txt', 'w') as h:
        h.write('-------HighestScorers---------\n\n')
        for sub, roll_mark in highest.items():              # taking subject and roll and marks
            roll, mark = roll_mark
            name = data[roll]['name']                       # names
            all = []
            for r, e in data.items():                    # data items in r and e
                if e['marks'][sub] == mark:
                    all.append(e['name'])
            h.write(f'{sub}\t\t:\t\t{all} scored {mark}\n')
    print('created highest.txt')


main()                                        # calling main
