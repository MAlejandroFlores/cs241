'''
Checkpoint 09A
Alejandro Flores Medina
CS241
'''

def main():
    valid_input = False
    while not valid_input:
        try:
            number1 = input("Enter a number: ")
            number1 = int(number1)
            valid_input = True

        except ValueError:
            print("The value entered is not valid")

    print("The result is: {}".format(number1*2))

if __name__ == "__main__":
    main()
