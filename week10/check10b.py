"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Alejandro Flores Medina
Merge sort
Sorts a list of numbers.
"""


def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    if len(numbers) > 1:
        mid = len(numbers)//2 # Half index of the list
        left_list = numbers[:mid]
        right_list = numbers[mid:]

        sort(left_list)
        sort(right_list)

        i = 0  # left list index
        j = 0  # right list index
        k = 0  # merge list index

        '''
        Case 1: Existing left side and a right side.
        '''
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                numbers[k] = left_list[i]
                i += 1  # Increase left list index
            else:
                numbers[k] = right_list[j]
                j += 1  # Increase right list index
            k += 1  # Increase merge list index

        '''
        Case 2: Only left case.
        '''
        while i < len(left_list):
            numbers[k] = left_list[i]
            i += 1  # Increase left list index
            k += 1  # Increase merge list index

        '''
        Case 3: Only right case.
        '''
        while j < len(right_list):
            numbers[k] = right_list[j]
            j += 1  # Increase left list index
            k += 1  # Increase merge list index


def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers


def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)


def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)


if __name__ == "__main__":
    main()
