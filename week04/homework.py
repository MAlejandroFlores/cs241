from collections import deque

class Song:
    def __init__(self):
        self.title = "Untitle"
        self.artist = "Unkown"

    def prompt(self):
        self.artist = input("Please enter an Artist name: ")
        self.title = input("Please enter a title name: ")

    def display(self):
        print(self.artist + " - " + self.title)


def main():
    playlist = deque()
    selection = 0

    while True:
        