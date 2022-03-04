class student:
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
    try:
        number = int(input('The student special number: '))

    except ValueError as err:
        print("Wrong character, enter a number.",err)
        number = int(input('The student special number: '))
    else:
        firstName = input("the first name: ")



# st1 = student(1, "ABDAllah", "ISMAILI", "DD101")
# print(st1.getNumber())
# print(st1.__str__())

addStudents()



