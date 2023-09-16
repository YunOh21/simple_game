import fn_show_text as show_text
import fn_prep as prep
import fn_map as map
import fn_play as play


show_text.intro_game()
you = prep.pick_your_color()
enemy = prep.set_the_enemy(you)
map.show_the_map(you, enemy)
prep.set_the_order(you, enemy)
play.play(you, enemy)
play.show_the_winner(you, enemy)
show_text.goodbye()