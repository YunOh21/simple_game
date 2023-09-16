from class_player import WhitePlayer, BlackPlayer
import random


def pick_your_color():
    your_color = input("If you are ready, pick the color. [B: black / W: white]")

    while your_color != 'chosen':
        if your_color == 'B':
            your_color = 'chosen'
            you = BlackPlayer()
        elif your_color == 'W':
            your_color = 'chosen'
            you = WhitePlayer()
        else:
            print(your_color)
            your_color = input("Sorry, the choice has to be B or W. Try again.")

    you.show_you()
    
    return you


def set_the_enemy(you):
    if isinstance(you, BlackPlayer):
        enemy = WhitePlayer()
    else:
        enemy = BlackPlayer()

    enemy.show_enemy()

    return enemy


def set_the_order(you, enemy):
    queue = [you, enemy]
    
    random.shuffle(queue)

    for i, v in enumerate(queue):
        if queue[i] == you:
            you.order = i  
        if queue[i] == enemy:
            enemy.order = i

    print("\n")
    print("The computer set the order for you and the enmemy.")

    if you.order == 0:
        print("Lucky you! You go first!")
    else:
        print("Your enemy goes first, and you are the second one.")