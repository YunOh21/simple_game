def draw_map():
    board_map = []

    for i in range(21):
        board_map.append(str(i))

    return board_map


def show_the_map(you, enemy):

    
    # 기존 icon을 지워주는 작업
    board_map = draw_map()

    # idx 가 20보다 큰 경우 20으로 만들어줌
    if you.idx > 20:
        you.idx = 20
    if enemy.idx > 20:
        enemy.idx = 20

    # you와 enemy가 같은 위치인 경우
    two_icons = you.icon + enemy.icon
    if enemy.idx == you.idx:
        board_map[you.idx] = two_icons
    
    # you와 enemy가 다른 위치인 경우
    else:
        board_map[you.idx] = you.icon
        board_map[enemy.idx] = enemy.icon

    print('you: ' + str(you.idx))
    print('enemy: ' + str(enemy.idx))
    print("Let's see the map.")
    print(board_map)