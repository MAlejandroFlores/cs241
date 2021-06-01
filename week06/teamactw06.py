class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def prompt_for_point(self):
        self.x = input("Enter x: ")
        self.y = input("Enter y: ")
        
    def display(self):
        print("(" + self.x + ", " + self.y + ")")

class Circle(Point):
    def __init__(self):
        super().__init__()
    
    def prompt_for_circle(self):
        super().prompt_for_point()
        self.radius = input("Enter radius: ")

    def display(self):
        print("Center:")
        super().display()
        print("Radius: " + self.radius)


def main():
    newCircle = Circle()
    newCircle.prompt_for_circle()
    print("")
    newCircle.display()


if __name__ == '__main__':
    main()

