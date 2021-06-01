''' 
    Alejandro Flores Medina
    Checkpoint B
    Inheritance
'''


''' Phone Class'''
class Phone:
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0
    
    def prompt_number(self):
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")

    def display(self):
        print("Phone info:")
        print("(" + self.area_code + ")" + self.prefix + "-" +self.suffix)
        
''' Smart Phone Class'''        
class SmartPhone(Phone):
    def __init__(self):
        super().__init__() # Call parent constructor
        self.email = "unkown@domain.com"

    def prompt(self):
        super().prompt_number() # Call parent method
        self.email = input("Email: ")

    def display(self):
        super().display() # Call parent method
        print(self.email)


def main():
    # Create a new Phone object
    newPhone = Phone()
    print("Phone:")
    newPhone.prompt_number()
    print("")
    newPhone.display()
    print("")

    # Create a new Smartphone object
    newSmartPhone = SmartPhone()
    print("Smart phone:")
    newSmartPhone.prompt()
    print("")
    newSmartPhone.display()

if __name__ == "__main__":
    main()