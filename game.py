from fn_show_text import intro_game, goodbye
from fn_prep import pick_your_color, set_the_enemy, set_the_order
from fn_map import show_the_map
from fn_play import play, show_the_winner


intro_game()
you = pick_your_color()
enemy = set_the_enemy(you)
show_the_map(you, enemy)
set_the_order(you, enemy)
play(you, enemy)
show_the_winner(you, enemy)
goodbye()