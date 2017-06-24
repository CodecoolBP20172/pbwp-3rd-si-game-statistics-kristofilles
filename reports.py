# Report functions
import csv


def count_games(file_name):
    num_lines = sum(1 for line in open('file_name'))
    return num_lines


def decide(file_name, year):
    datafile = file('file_name')
    found = False
    for line in datafile:
        if year in line:
            found = True
            break
    return found


def get_latest(filename="game_stat.txt"):
    f = open(filename, 'r')
    firstLine = f.readline().split("\t")
    max = firstLine[2]
    max_i = 1
    next(f)
    a = []
    for line in f:
        a = line.split("\t")
        if(max < a[2]):
            max = a[2]
            max_i = line
    return(max_i.split("\t")[0])


def count_by_genre(filename="game_stat.txt", genre="First-person shooter"):
    count = 0
    f = open(filename, 'r')
    for line in f:
        a = line.split("\t")
        if(genre == a[3]):
            count += 1
    return count


def get_line_number_by_title(filename="game_stat.txt", title="lófasz"):
    f = open(filename, 'r')
    lines = 0
    for line in f:
        a = line.split("\t")
        lines += 1
        if(a[0] == title):
            try:
                if (a[0] == title):
                    return lines
            except ValueError:
                return "There is no game with that title"





print(get_line_number_by_title(filename="game_stat.txt", title="lófasz"))
# if __name__ == "__main__":
#     main()
