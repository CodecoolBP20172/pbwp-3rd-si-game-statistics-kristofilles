# Report functions
import operator


def count_games(filename="game_stat.txt"):
    num_lines = sum(1 for line in open(filename))
    return num_lines


def decide(filename="game_stat.txt", year="2000"):
    f = open(filename, 'r')
    for line in f:
        if str(year) in line:
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
    games = f.readlines()
    titles = [title.split('\t')[0] for title in games]
    try:
        line_number_of_title = titles.index(title) + 1
        return line_number_of_title
    except ValueError:
        return('There is no game with the given name')


def sort_abc(filename="game_stat.txt"):
    abc_list = []
    f = open(filename, 'r')
    for line in f:
        a = line.split("\t")
        abc_list.append(a[0])
    return sorted(abc_list)


def get_genres(filename="game_stat.txt"):
    genre_set = set()
    f = open(filename, 'r')
    for line in f:
        a = line.split("\t")
        genre_set.add(a[3])
    return sorted(genre_set, key=str.lower)


def when_was_top_sold_fps(filename="game_stat.txt"):
    fps_year = {}
    f = open(filename, 'r')
    for line in f:
        a = line.split("\t")
        if a[3] == "First-person shooter":
            fps_year[int(a[2])] = float(a[1])
    if fps_year == {}:
        raise ValueError("No such genre in the input file.")
    sorted_dict = sorted(fps_year.items(), key=operator.itemgetter(1))
    return sorted_dict[-1][0]
