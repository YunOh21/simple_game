from fn_map import show_the_map


def go(player):
    print("\n")
    dice_number = player.roll_the_dice()
    player.move(dice_number)


def roll_the_dice(you, enemy):
    if you.order == 0:
        go(you)
        show_the_map(you, enemy)
        
        if you.idx < 20:
            go(enemy)
            show_the_map(you, enemy)

    else:
        go(enemy)
        show_the_map(you, enemy)
        
        if enemy.idx < 20:
            go(you)
            show_the_map(you, enemy)


def play(you, enemy):
    while you.idx < 20 and enemy.idx < 20:
        roll_the_dice(you, enemy)

        if you.idx == 20 or enemy.idx == 20:
            break
        elif input("Will you roll the dice again? [Y/N]") == "N":
            break


def show_the_winner(you, enemy):
    winner = max(you.idx, enemy.idx, 20)
    if winner == you.idx:
        print("Bravo! You won!")
    elif winner == enemy.idx:
        print("The winner is your enemy.")
    else:
        print("Sorry to hear that playtime is over. \U0001F622")