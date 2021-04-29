def prompt_filename():
    file_name = input('Please enter a filename: ')
    return file_name


def parse_file(filename, word_to_find):
    word_count = 0
    with open(filename) as file:
        file_data = file.read()
        lines = file_data.split('\n')
        for line in lines:
            words = line.split()
            for word in words:
                # if word.lower().strip('.') == 'pride':
                if word.lower().strip('.') == word_to_find:
                    word_count += 1 

    return word_count
    

def prompt_word():
    word = input('Which word do you want to search: ')
    return word


def main():
    filename = prompt_filename()
    print('Opening ' + filename)
    word_to_find = prompt_word()
    count = parse_file(filename, word_to_find)
    print('The word ' + word_to_find + ' occurs ' + str(count) + ' times in this file')
        
if __name__ == "__main__":
    main()