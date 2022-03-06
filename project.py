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
class subject:
    Subjects = []
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
                    self.__examType = "ctrl"
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

        controlFile = open("ConFile.txt", "a")
        for i in subject.Subjects:
            controlFile.write(i.__str__())

    def studentsExams(self):
        controlsNumber = len(subject.Subjects)
        studentsNumber = len(student.Students)
        print(controlsNumber)
        print(studentsNumber)


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
            print("Your group have " + str(number) + " students.")

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
    print("6- To add a new student.")
    print("7- For calculate exams final marks.")
    print("8- For exporting your file.")
    print("9- End tasks." + "\n")

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
    else:
        print("Ended.")
        break



