def prompt_filename():
    file_name = input('Please enter a filename: ')
    return file_name

def main():
    filename = prompt_filename()
    print('Opening ' + filename)
    parse_file(filename)

def parse_file(filename):
    pride_count = 0
    with open(filename) as file:
        file_data = file.read()
        lines = file_data.split('\n')
        for line in lines:
            words = line.split()
            for word in words:
                if word.lower().strip('.') == 'pride':
                    pride_count += 1 
    print('The word pride occurs ' + str(pride_count) + ' times in this file')
        
if __name__ == "__main__":
    main()