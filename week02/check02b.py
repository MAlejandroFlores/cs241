
def readsFileName():
    filename = input('Enter file: ')
    return filename

def getLinesCount(file):
    lines_count = 0
    lines = file.split('\n')
    lines_count = len (lines)
    # if last line is blank rest it from count
    if (lines[-1] == ''):
        lines_count -= 1
    return lines_count

def getWordsCount(file):
    words_count = 0
    lines = file.split('\n')
    # Iterate over lines
    for line in lines:
        words = line.split()
        words_count += len(words)
    return words_count

def main():
    filename = readsFileName()
    with open(filename) as file:
        file_data = file.read()
        lines = getLinesCount(file_data)
        words = getWordsCount(file_data)
        print('The file contains ' + str(lines) + ' lines and ' + str(words) + ' words.')

main()
