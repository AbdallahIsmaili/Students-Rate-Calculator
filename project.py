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

    for i in st1.Students:
        print(i.__str__())
        # print(i.getFirstName())

addStudents = staticmethod(addStudents)


# print(st1.getNumber())
# print(st1.__str__())

addStudents()



