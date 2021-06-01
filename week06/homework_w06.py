from collections import deque

class Student():
    def __init__(self) -> None:
        self.name = "No name"
        self.course = "No course"

    def prompt(self):
        pass

    def display(self):
        pass


class HelpSystem():
    def __init__(self) -> None:
        self.waiting_list = deque()

    def is_student_waiting(self):
        return self.waiting_list.__len__ != 0

    def is_student_waiting(self, Student):
        pass