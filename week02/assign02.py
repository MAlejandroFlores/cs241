def prompt_filename():
    filname = input('Please enter the data file: ')
    return filname

def read_file(filename):
    with open(filename) as file:
        file_data = file.read()
        lines = file_data.split('\n')
        for line in lines:
            columns = line.split(',')
            

def main():
    filename = prompt_filename()
    read_file(filename)



if __name__ == "__main__":
    main()
