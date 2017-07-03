from pprint import pprint
from reports import *

pprint(get_most_played('game_stat.txt'))
pprint(sum_sold('game_stat.txt'))
pprint(get_selling_avg('game_stat.txt'))
pprint(count_longest_title('game_stat.txt'))
pprint(get_date_avg('game_stat.txt'))
pprint(count_grouped_by_genre('game_stat.txt'))
