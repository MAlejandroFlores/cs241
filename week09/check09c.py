'''
Checkpoint 09B
Alejandro Flores Medina
CS241
'''


class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)

def get_inverse_B(number):
    if number < 0:
        raise NegativeNumberError("NegativeNumberError")
    

def get_inverse(number):
    inverse = 0

    number = int(number)
    inverse = 1 / number
    get_inverse_B(number)
    return inverse

def main():
    number = input("Enter a number: ")

    try:
        inverse = get_inverse(number)
        print("The result is: {}".format(inverse))
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError:
        print("Error: The value cannot be negative")


if __name__ == "__main__":
    main()
