# Printing functions

from reports import *


def printing():
    print(get_latest(filename="game_stat.txt"))
    print(count_games(filename="game_stat.txt"))
    print(decide(filename="game_stat.txt", year="2000"))
    print(get_latest(filename="game_stat.txt"))
    print(count_by_genre(filename="game_stat.txt", genre="First-person shooter"))
    print(get_line_number_by_title(filename="game_stat.txt", title="lófasz"))
    print(sort_abc(filename="game_stat.txt"))
    print(get_genres(filename="game_stat.txt"))
    print(when_was_top_sold_fps(filename="game_stat.txt"))


printing()
