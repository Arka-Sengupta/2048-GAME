from logic import *
def main():
    board = initialise_board()
    while True:
        display_board(board)
        if check_win(board) is True:
            print("You Won the game")
            break
        if check_lose(board) is True:
            print("You Lose")
            break
        user_move = input("Press W/A/S/D for swiping up/left/down/right: ").lower()
        if user_move =="w":
            board = swipe_up(board)
        elif user_move == "a":
            board = swipe_left(board)
        elif user_move == "s":
            board = swipe_down(board)
        elif user_move == "d":
            board = swipe_right(board)
        else:
            print("Invalid move")
            continue
        add_new_tile(board)
if __name__ == "__main__":
    main()
