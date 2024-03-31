


players = ["O", "X"]
board = [["", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]


def print_board(board): 
    print(f"""      {board[0][0]} | {board[0][1]} | {board[0][2]}
    -----------
     {board[1][0]} | {board[1][1]} | {board[1][2]}
    -----------
     {board[2][0]} | {board[2][1]} | {board[2][2]}
    """)
    
    
def check_winner(board):
    if board[0][0] != " " and (board[0][0] == board[0][1] == board[0][2] or board[0][0] == board[1][0] == board[2][0] or board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    elif board[1][1] != " " and (board[1][1] == board[0][1] == board[2][1] or board[1][1] == board[1][0] == board[1][2] or board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]
    elif board[2][2] != " " and (board[2][2] == board[2][1] == board[2][0] or board[2][2] == board[0][2] == board[1][2]):
        return board[2][2]
    else:
        return None

# def place_turn(board, x, y):
#     board[y][x] = "X"
#     return board

def play_turn(board):
    round_num = 0
    while True:
        print_board(board)
        position = int(input("choose a number form 1-9: "))
        x = (position - 1)%3
        y = (position - 1)//3
        
        board[y][x] = players[round_num%2]
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} WON!")
            break
        
        round_num += 1


if __name__ == "__main__":
    play_turn(board)