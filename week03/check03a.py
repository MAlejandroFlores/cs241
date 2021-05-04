# Alejandro Flores Medina
# CS241

'''
Student Class
'''
class Student:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.id = 0

    def setFirstName(self, firstName):
        self.firstName = firstName
    
    def setLastName(self, lastName):
        self.lastName = lastName

    def setId(self, id):
        self.id = id

    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName

    def getId(self):
        return self.id
        
def prompt_student():
    newStudent = Student()
    firstName = input('Please enter your first name: ')
    lastName = input('Please enter your last name: ')
    id = input('Please enter your id number: ')
    newStudent.setFirstName(firstName)
    newStudent.setLastName(lastName)
    newStudent.setId(id)
    return  newStudent

def display_student(Student):
    print('\nYour information:')
    print( str(Student.getId()) + ' - ' + Student.getFirstName() + ' ' + Student.getLastName())

def main():
    newStudent = prompt_student()
    display_student(newStudent)

if __name__ == "__main__":
    main()
