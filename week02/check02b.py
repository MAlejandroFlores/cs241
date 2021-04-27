
def readsFileName():
    filename = input('Enter file: ')
    return filename

def getLinesCount(file):
    lines_count = 0
    for line in file:
            line = line.split('\n')
            lines_count += 1
    return lines_count

def getWordsCount(file):
    words_count = 0
    words = file.split(' ')
    return len(words)

def main():
    filename = readsFileName()
    with open(filename) as file:
        lines = getLinesCount(file)
        words = getWordsCount(file)
        print('The file contains {} lines and {} words.', lines, words)

main()
