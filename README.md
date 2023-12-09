# 소개
![image](https://github.com/YunOh21/simple_game/assets/86283716/1f53b66d-0159-4e91-94a4-25cd3e74aec2)

- 파이썬 클래스 개념 실습용 미니 프로젝트입니다.
- 부루마블 류의 보드게임을 상정해서 만들었습니다.
- 정리한 내용: https://velog.io/@yun5/간단한-보드게임-만들기

# 게임의 규칙
- 플레이어의 말은 흰색과 검은색
    - Player라는 베이스 클래스를 바탕으로, 그를 상속한 클래스가 WhitePlayer와 BlackPlayer
- 게임을 시작할 때 말의 색상 선택
- '나'와 적의 현재 위치를 list를 활용해서 화면에 표시
- 주사위를 굴리는 순서는 게임 초기에 랜덤 설정
- 매 턴마다 1부터 6사이의 값을 가지는 주사위를 굴린다.
- 숫자 20에 먼저 도착하는 플레이어가 이기고, 이때 게임 종료
- 또는 '나'가 주사위 굴리기를 거절할 때 게임 종료

# 파일

## 실행
- game.py

## 클래스
- class_player.py
    - Player: Base Class
    - WhitePlayer, BlackPlayer: Inherited Class

## 함수
### 1. fn_show_text.py
- 안내문구 함수
    - intro_game
    - goodbye

### 2. fn_prep.py
- 게임 실행 준비
    - pick_your_color
    - set_the_enemy
    - set_the_order

### 3. fn_map.py
- 지도 그리는 함수
    - draw_map
    - show_the_map

### 4. fn_play.py
- 게임 플레이
    - go
    - roll_the_dice
    - play
    - show_the_winner
