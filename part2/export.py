from reports import *


def export_text(input_file, export_file):
    export_list = [get_most_played('game_stat.txt'),
                   sum_sold('game_stat.txt'),
                   get_selling_avg('game_stat.txt'),
                   count_longest_title('game_stat.txt'),
                   get_date_avg('game_stat.txt'),
                   count_grouped_by_genre('game_stat.txt')]
    path = "/home/kristof/codecool/cloned_repos/pbwp-3rd-si-game-statistics-kristofilles/part2%s" % export_file
    with open(path, "w") as text:
        for item in export_list:
            text.write(str(item)+"\n")


export_text("game_stat.txt", "export.txt")
