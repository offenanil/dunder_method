# from IPython.display import clear_output
def display_board(board):
    # def clear():
    #     os.system('clear')
    print(' | |')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(' | |')
    print('-----')
    print(' | |')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(' | |')
    print('-----')
    print(' | |')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(' | |')
test_board = ['#', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
display_board(test_board)
def player_input():
    '''takaing input from the user either 'o' or 'x'
    output = (player1 marker, player 2 marker)
    '''
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input('player1: choose x or o: ').lower()
    if marker == 'x':
        return ('x', 'o')
    else:
        return ('o', 'x')
def place_marker(board, marker, position):
    board[position] = marker
place_marker(test_board, '$', 8)
display_board(test_board)
def win_check(board, mark):
    '''for win: all rows share the same marker
    and all columns check match and 2 diagonals AS WELL
    '''
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    # across first column
    (board[8] == mark and board[5] == mark and board[2] == mark) or
     # across the second column
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    # across the third column
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    # across the diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))
#             across the diagonal
display_board(test_board)
# checking the function
win_check(test_board, 'x')
import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'player1'
    else:
        return  'player 2'
def space_check(board, position):
    '''indicating whether a space on the board is freely available
    '''
    return board[position] == ' '
def full_board_check(board):
#     checking if the board is full and returns a boolean value. True if full and False otherwise
    for i in range(1, 10):
        if space_check(board, i):
            return False

#         board is full if we return true
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

        if not replay():
            break








