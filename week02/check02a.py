

def prompt_number():
    number = -1
    while number < 0:
         number = int(input('Enter a positive number: '))
         if number < 0:
             print('Invalid entry. The number must be positive.')
    return number


def compute_sum(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg


def main():
    sum = 0
    for tries in range(3):
        sum = sum + prompt_number()
        print()
    print ('The sum is: ' + str(sum))

main()
