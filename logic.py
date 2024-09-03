import random
def initialise_board():
    board = [["_"]*4 for x in range(4)]           #making a 4X4 matrix filled with 0 and two 2s at
    add_new_tile(board)                         #random positions
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_positions=[(i,j) for i in range(4) for j in range(4) if board[i][j]=="_"]
    if empty_positions:
        i,j = random.choice(empty_positions)
        board[i][j] = 2

def display_board(board):
    for row in board:
        print("\t".join(map(str,row)))
        print()

def merge_left(row):
    new_row=[i for i in row if i != "_"]  #removing 0s
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i+1]:
            new_row[i] *=2              #doubling the i'th term
            new_row[i+1] = "_"            #making the i+1 st term 0
    new_row = [i for i in new_row if i !=0] #removing 0s
    return new_row + ["_"]*(4-len(new_row))   #filling the extra spaces with 0s
def swipe_left(board):
    new_board = [merge_left(row) for row in board]
    return new_board
def swipe_right(board):
    new_board = [list(reversed(row)) for row in board]      #we are here reversing the matrix
    new_board = swipe_left(new_board)
    new_board = [list(reversed(row)) for row in new_board]
    return new_board
def transpose(board):
    return[list(row) for row in zip(*board)]    #zip function is being used here which is repacking
def swipe_up(board):                            #the separate itenaries ie. rows and converting them
    new_board = transpose(board)                #into individual collumns ie. just like transposing 
    new_board = swipe_left(new_board)           #a matrix
    new_board = transpose(new_board)
    return new_board
def swipe_down(board):
    new_board = transpose(board)
    new_board = swipe_right(new_board)
    new_board = transpose(new_board)
    return new_board
def check_win(board):
    for row in board:
        if 2048 in row:
            return True
        else:
            return False
def check_lose(board):
    for row in board:
        if "_" in row:
            return False
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1] or board[j][i] == board[j+1][i]:
                return False
    return True
# def main():
#     board = initialise_board()
#     while True:
#         display_board(board)
#         if check_win(board) is True:
#             print("You Won the game")
#             break
#         if check_lose(board) is True:
#             print("You Lose")
#             break
#         user_move = input("Press W/A/S/D for swiping up/left/down/right: ").lower()
#         if user_move =="w":
#             board = swipe_up(board)
#         elif user_move == "a":
#             board = swipe_left(board)
#         elif user_move == "s":
#             board = swipe_down(board)
#         elif user_move == "d":
#             board = swipe_right(board)
#         else:
#             print("Invalid move")
#             continue
#         add_new_tile(board)
# if __name__ == "__main__":
#     main()