from csv import reader


def prompt_filename():
    filname = input('Please enter the data file: ')
    return filname


def read_file(filename):
    data_array = []
    with open(filename) as file:
        data_lines = reader(file)
        # read the file to a list of lists
        data_array = list(data_lines)

    # Strip off the first row
    data_array.pop(0)
    return data_array


def get_avg_rate(data_lines):
    sum = 0
    list_size = len(data_lines)
    for line in data_lines:
        comm_rate = float(line[6])
        sum += comm_rate
    avg_rate = sum / list_size
    return avg_rate


def get_highest_rate_index(data_lines):
    highest_rate = 0
    highest_rate_i = 0
  
    for num, row in enumerate(data_lines):
        comm_rate = float(row[6])
        if comm_rate > highest_rate:
            highest_rate = comm_rate
            highest_rate_i = num

    return highest_rate_i


def get_lowest_rate_index(data_lines):
    lowest_rate_i = 0
    lowest_rate = 1000

    for num, row in enumerate(data_lines):
        comm_rate = float(row[6])
        if comm_rate < lowest_rate:
            lowest_rate = comm_rate
            lowest_rate_i = num

    return lowest_rate_i


def main():
    UTILITY_NAME = 2
    ZIPCODE = 0
    STATE = 3
    RATE = 6

    filename = prompt_filename()
    data_lines = read_file(filename)
    avg_rate = get_avg_rate(data_lines)

    highest_rate_i = get_highest_rate_index(data_lines)
    highest_rate = data_lines[highest_rate_i]

    lowest_rate_i = get_lowest_rate_index(data_lines)
    lowest_rate = data_lines[lowest_rate_i]

    print('\nThe average commercial rate is: ' + str(avg_rate))

    print('\nThe highest rate is:')
    print(highest_rate[UTILITY_NAME] + ' (' + highest_rate[ZIPCODE] + ', ' + highest_rate[STATE] \
          + ') - $' + highest_rate[RATE])

    print('\nThe lowest rate is:')
    print(lowest_rate[UTILITY_NAME] + ' (' + lowest_rate[ZIPCODE] + ', ' + lowest_rate[STATE] \
          + ') - ${:.1f}'.format(float(lowest_rate[RATE])))



if __name__ == "__main__":
    main()
