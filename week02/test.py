class student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.identification = 0

    def prompt_student(self):
        self.first_name = input("Please enter your first name: ")
        self.last_name = input("Please enter your last name: ")
        self.identification = input("Please enter your id number: ")

    def display_student(self):
        print("")
        print("Your information:")
        print(f"{self.identification} - {self.first_name} {self.last_name}")

def main():
    usuario = student()
    usuario.prompt_student()
    usuario.display_student() 

if __name__ == "__main__":
    main()