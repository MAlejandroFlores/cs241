##
# Author: Alejandro Flores Medina
##

from csv import reader

'''
  NAME: prompt_filename
  PURPOSE: Aks for a csv filename
  INPUT: None
  OUTPUT: returns the filname given by the user
'''
def prompt_filename():
    filname = input('Please enter the data file: ')
    return filname


'''
  NAME: read_file
  PURPOSE: Open up a file and save it into a List variable
  INPUT: filename
  OUTPUT: List of list with all information from csv file without the header row
'''
def read_file(filename):
    data_array = []
    with open(filename) as file:
        data_lines = reader(file)
        # read the file to a list of lists
        data_array = list(data_lines)

    # Remove off the header first row
    data_array.pop(0)
    return data_array


'''
  NAME: get_rate
  PURPOSE: Iterates over csv file, get the highest, lowest index rates, and average comm_rate
  INPUT: List of Lists rows company name, zipcode, state, rate, etc
  OUTPUT: List with 3 variables, lowest rate line index, highest rate line index, average comm rate
'''
def get_rates(data_lines):
    # Variables for HIGHEST rate
    highest_rate = 0
    highest_rate_i = 0
    # Variables for LOWEST rate
    lowest_rate_i = 0
    lowest_rate = 1000
    # Variables for AVERAGE rate
    sum = 0
    list_size = len(data_lines)
    # Iterate over the whole list
    for num, row in enumerate(data_lines):
        comm_rate = float(row[6])
        # Find the Highest rate
        if comm_rate > highest_rate:
            highest_rate = comm_rate
            highest_rate_i = num
        # Find the Lowest rate
        if comm_rate < lowest_rate:
            lowest_rate = comm_rate
            lowest_rate_i = num
        # Sum rate to calculate Average
        sum += comm_rate
    avg_rate = sum / list_size
    return [lowest_rate_i, highest_rate_i, avg_rate]

'''
  NAME: print_rates
  PURPOSE: Print the highest, lowest and average rates
  INPUT: List lowest rate row, highest rate row, average rate calculated
  OUTPUT: Print screen rates
'''
def print_rates(lowest_rate, highest_rate, avg_rate):
    # Variables for column numbers indexes
    UTILITY_NAME = 2
    ZIPCODE = 0
    STATE = 3
    RATE = 6
    # Print rates gather
    print('\nThe average commercial rate is: ' + str(avg_rate))

    print('\nThe highest rate is:')
    print(highest_rate[UTILITY_NAME] + ' (' + highest_rate[ZIPCODE] + ', ' + highest_rate[STATE]
          + ') - $' + highest_rate[RATE])

    print('\nThe lowest rate is:')
    print(lowest_rate[UTILITY_NAME] + ' (' + lowest_rate[ZIPCODE] + ', ' + lowest_rate[STATE]
          + ') - ${:.1f}'.format(float(lowest_rate[RATE])))

'''
  MAIN Function
'''
def main():
    # Prompt for filname and parse data to a List
    filename = prompt_filename()
    data_lines = read_file(filename)

    # Get rates variables
    rates = get_rates(data_lines)
    lowest_rate_i = rates[0]
    highest_rate_i = rates[1]
    avg_rate = rates[2]

    # Lowest rate row
    lowest_rate = data_lines[lowest_rate_i]
    # Highest rate row
    highest_rate = data_lines[highest_rate_i]

    # Print the rates
    print_rates(lowest_rate, highest_rate, avg_rate)


if __name__ == "__main__":
    main()
