class student:
    Students = []
    def __init__(self,number, firstName, lastName, group):
        self.__number = number
        self.__firstName = firstName
        self.__lastName = lastName
        self.__group = group

    def __str__(self) -> str:
        return str(self.__number) + " | " + self.__firstName + " " + self.__lastName + " | " + str(self.__group)

    def getNumber(self):
        return self.__number

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getGroup(self):
        return self.__group

#/////////////////////////////////////////////////////////////////////////////////////////////

import datetime
import calendar
import re

class subject:
    Subjects = []
    examList = []
    mySearch = []

    def __init__(self,examNumber, subjectName, date, teacher, examType):
        self.__examNumber = examNumber
        self.__subjectName = subjectName
        self.__date = date
        self.__teacher = teacher
        self.__examType = examType

    def __str__(self) -> str:
        return self.__examType +" N." + str(self.__examNumber) + " | " + self.__subjectName + " at " + str(self.__date) + " ,By Mr." + self.__teacher

    def getExamNumber(self):
        return self.__examNumber

    def getSubjectName(self):
        return self.__subjectName

    def getControlDate(self):
        return self.__date

    def getTeacherName(self):
        return self.__teacher

    def getExamType(self):
        return self.__examType


    def setExamNumber(self):
        trying = "con"
        while trying != "stp":
            try:
                self.__examNumber = int(input("Control number ..? : "))
            except ValueError as Err:
                print("Please enter a number ...", Err)
                continue
            else:
                break

    def setSubjectName(self):
        trying = "con"
        while trying != "stp":
            try:
                self.__subjectName = input("Subject name ..? : ")
            except ValueError as Err:
                print("Please enter your subject name ...", Err)
                continue
            else:
                break

        self.__subjectName = self.__subjectName.title()

    def setControlDate(self):
        year = datetime.datetime.now().year
        day = 1
        month = 1

        trying = "con"
        while trying != "stp":
            try:
                month = int(input("Enter Exam month ..? : "))
            except ValueError as Err:
                print("Please enter the exam month ...", Err)
                continue
            else:
                print("\n" + calendar.month(year, month))
                break

        trying = "con"
        while trying != "stp":
            try:
                day = int(input("Enter Exam day ..? : "))
            except ValueError as Err:
                print("Please enter the exam day ...", Err)
                continue
            else:
                break

        self.__date = datetime.datetime(year, month, day).date()

    def setTeacherName(self):
        trying = "con"
        while trying != "stp":
            try:
                self.__teacher = input("Professor name ..? : ")
            except ValueError as Err:
                print("Please enter the professor name ...", Err)
                continue
            else:
                break

    def setExamType(self):
        trying = "con"
        while trying != "stp":
            try:
                self.__examType = input("Exam Type (C 'Control', E 'EFM'..? ) : ")
            except ValueError as Err:
                print("Please enter your subject name ...", Err)
                continue
            else:
                if self.__examType.upper() == "C":
                    self.__examType = "Ctrl"
                    break
                elif self.__examType.upper() == "E":
                    self.__examType = "EFM"
                    break
                else:
                    continue

    def createExam(self):
        trying = "con"
        while trying != "stp":
            try:
                self.__teacher = input("Professor name ..? : ")
            except ValueError as Err:
                print("Please enter the professor name ...", Err)
                continue
            else:
                break

        adding = "add"
        while adding != "stp":
            con = subject(0, "subjectName", "01-01-2022", self.__teacher, "type")

            con.setExamType()
            con.setExamNumber()
            con.setSubjectName()
            con.setControlDate()
            #con.setTeacherName()

            trying = "con"
            while trying != "stp":
                try:
                    adding = input("add another exam? (stp to stop):  ")
                except ValueError as Err:
                    print("Enter your choose (stp to stop / add to add another) :", Err)
                    continue
                else:
                    subject.Subjects.append(con)
                    break

        print("\n")
        for i in subject.Subjects:
            print(i.__str__())

        controlFile = open("Control.txt", "a")
        for i in subject.Subjects:
            controlFile.write(i.__str__())
            controlFile.write('\n')

    def studentsExams(self):

        controlNote = ""
        studentFullName = ""
        for line in student.Students:
            studentFullName = str(line.getNumber()) + " " + line.getFirstName() + " " + line.getLastName()
            print("\n" + studentFullName + " EXAMS NOTES.")

            for i in subject.Subjects:
                theExam = i.getExamType() + ".N" + str(i.getExamNumber())

                note = 1
                trying = "con"
                while trying != "stp":
                    try:
                        note = float(input(theExam + " Note: "))
                    except ValueError as Err:
                        print("unavailable note ", Err)
                        continue
                    else:
                        if i.getExamType() == "C" or i.getExamType() == "Ctrl":
                            if note < 0 or note > 20:
                                print("the note should be between 0 and 20.")
                                continue
                            else:
                                break
                        elif i.getExamType() == "E" or i.getExamType() == "EFM":
                            if note < 0 or note > 40:
                                print("the note should be between 0 and 40.")
                                continue
                            else:
                                break

                controlNote += theExam + " = " + str(note) + " | "

            fullNote = str(studentFullName + " Notes: " + controlNote)
            subject.examList.append(fullNote)
            controlNote = ''

        print("The marks you have added.. \n")
        for i in subject.examList:
            print(i)

        controlFile = open("Marks.txt", "a")
        for i in subject.examList:
            controlFile.write(i.__str__())
            controlFile.write('\n')

    def searchOnDegree(self):

        searchedGroup = input("Your student group: ")
        thoseStudents = []

        searchedGroup = searchedGroup.upper()

        for i in student.Students:
            thisStudent = re.findall("DD101", str(i))
            group = ''.join(str(e) for e in thisStudent)
            if str(group) == searchedGroup.strip():
                print(i)
                thoseStudents.append(str(i))
            else:
                print("There is no student.")

        print("Choose The student by his number please.")
        searchedNumber = int(input("Enter the student number: "))

        for i in subject.examList:
            if i[0] == str(searchedNumber):
                subject.mySearch.append(str(i))
                print(i)

    def changeDegree(self):

        subject.searchOnDegree(self)

        toChange = subject.mySearch
        print(toChange)
        trying = "on"
        while trying != "off":

            for i in range(0, len(toChange)):
                result = re.findall("\d+\.\d+", str(toChange))
                NumberOfCon = len(result)
                print("\n")
                print("The number of controls and EFM is: ", NumberOfCon)
                print("Your Notes: " + ''.join(str(e + " ,  ") for e in result))
                break
            break

        controlNote = ""
        studentFullName = ""
        for line in student.Students:
            studentFullName = str(line.getNumber()) + " " + line.getFirstName() + " " + line.getLastName()
        print("\n" + studentFullName + " NEW EXAMS NOTE PLEASE...!")

        for i in subject.Subjects:
            theExam = i.getExamType() + ".N" + str(i.getExamNumber())

            note = 1
            trying = "con"
            while trying != "stp":
                try:
                    note = float(input(theExam + " Note: "))
                except ValueError as Err:
                    print("unavailable note ", Err)
                    continue
                else:
                    if i.getExamType() == "C" or i.getExamType() == "Ctrl":
                        if note < 0 or note > 20:
                            print("the note should be between 0 and 20.")
                            continue
                        else:
                            break
                    elif i.getExamType() == "E" or i.getExamType() == "EFM":
                        if note < 0 or note > 40:
                            print("the note should be between 0 and 40.")
                            continue
                        else:
                            break

            controlNote += theExam + " = " + str(note) + " | "

            fullNote = str(studentFullName + " Notes: " + controlNote)
            subject.examList.append(fullNote)
            controlNote = ''

        print("\n The marks have been added.. \n")

        print("     REMOVE THE OLD MARKS INFORMATION PLEASE! \n")
        print(subject.examList)

        print(subject.examList[0])
        print("\n")
        index = 0
        trying = "con"
        while trying != "stp":
            try:
                index = int(input("The old mark information index in the table is: \n choose between 1 and , " + str(len(subject.examList)) + ": "))
                while index < 1 or index > len(subject.examList):
                    index = int(input("Re enter the index please: \n should be among 1 and , " + str(
                        len(subject.examList)) + ": "))
                del subject.examList[index-1]

            except ValueError as Err:
                print("unavailable index ", Err)
                continue
            else:
                break

        for i in subject.examList:
            print(i)

        controlFile = open("Marks.txt", "a")
        for i in subject.examList:
            controlFile.write(i.__str__())
            controlFile.write('\n')

    def calculateMarks(self):
        #subject.searchOnDegree(self)

        #toCalcule = subject.mySearch

        toCalcule = subject.examList

        calculeResult  = ''.join(str(e + " ,  ") for e in toCalcule)
        print(calculeResult)

        for i in subject.examList:
            trying = "on"
            moy = 0
            while trying != "off":
                for j in range(0, len(toCalcule)):
                    result = re.findall("\d+\.\d+", str(i))

                    som = 0
                    div = len(result)

                    for i in result:
                        som += float(i)
                    moy = som / div

                    NumberOfCon = len(result)
                    print("\n")
                    print("The number of controls and EFM is: ", NumberOfCon)
                    print("Your Notes: " + ''.join(str(e + " ,  ") for e in result))
                    break
                print(''.join(str(e + " ,  ") for e in i) + " | MODULE MOY: " + str(moy))
                break


def addStudents():
    print('ADD STUDENTS INFORMATIONS')
    number = 1
    st1 = ""
    group = input("The group of your students: ")
    print("here your group...: ", group.upper())

    adding = "add"
    while adding != "stp":
        firstName = input("The first name of the student: ")
        lastName = input("The last name of the student: ")

        st1 = student(number, firstName.upper(), lastName.upper(), group.upper())
        student.Students.append(st1)
        adding = input("add another student? (stp to stop): ")
        if adding != "stp":
            number += 1
        else:
            print("\n Your group have " + str(number) + " students.")

    for i in student.Students:
        print(i.__str__())

    groupStudents = open(group.upper(), "a")
    for i in student.Students:
        groupStudents.write(str(i))
        groupStudents.write("\n")



addStudents = staticmethod(addStudents)

choosing = "choose"
while choosing != "exit":
    print("\n"+"HI THERE USER!" + "\n")
    print("1- For declare your group name and add students.")
    print("2- For add a new subject.")
    print("3- For add exams and students degrees.")
    print("4- For search on a student degree.")
    print("5- For change a student mark.")
    print("6- For calculate exams final marks.")
    print("7- For exporting your file.")
    print("8- End tasks." + "\n")

    choseNumber = 0
    trying = "con"
    while trying != "stp":
        try:
            choseNumber = int(input("Enter Here:"))

        except ValueError as Err:
            print("Try to enter a number please: ")
            continue
        else:
            break

    con = subject(1, "subjectName", "01-01-2022", "teacher", "type")
    if choseNumber == 1:
        addStudents()

    elif choseNumber == 2:
        con.createExam()

    elif choseNumber == 3:
        con.studentsExams()

    elif choseNumber == 4:
        con.searchOnDegree()

    elif choseNumber == 5:
        con.changeDegree()

    elif choseNumber == 6:
        con.calculateMarks()

    else:
        print("Ended.")
        break





