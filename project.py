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
        st1.Students.append(st1)
        adding = input("add another student? (stp to stop): ")
        if adding != "stp":
            number += 1
        else:
            print("Your group have "+ str(number) +" students.")

    groupStudents = open(group.upper(), "a")
    for i in st1.Students:
        groupStudents.write(str(i))
        groupStudents.write("\n")
        #print(i.__str__())




addStudents = staticmethod(addStudents)

choosing = "choose"
while choosing != "exit":
    print("\n"+"HI THERE USER!" + "\n")
    print("1- For declare your group name and add students.")
    print("2- For add a new subject.")
    print("3- For add exams and degrees.")
    print("4- For search on a degree.")
    print("5- For change a mark.")
    print("6- to add a new student.")
    print("7- For exporting your file.")
    print("8- End tasks." + "\n")

    choseNumber = 0
    trying = "con"
    while trying != "stp":
        try:
            choseNumber = int(input("Enter Here:"))

        except ValueError as Err:
            print("Try to enter a number please: ")
            trying = "con"
        else:
            break

    if choseNumber == 1:
        addStudents()
    else:
        print("Ended.")
        break



