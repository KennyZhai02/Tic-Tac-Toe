import random

def print_board(board):
    """Prints the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_empty_positions(board):
    """Returns a list of empty positions on the board."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def computer_move(board):
    """Determines the computer's move."""
    # Try to win
    for r, c in get_empty_positions(board):
        board[r][c] = "O"
        if check_winner(board, "O"):
            return
        board[r][c] = " "
    
    # Block the human
    for r, c in get_empty_positions(board):
        board[r][c] = "X"
        if check_winner(board, "X"):
            board[r][c] = "O"
            return
        board[r][c] = " "
    
    # Random move
    r, c = random.choice(get_empty_positions(board))
    board[r][c] = "O"

def human_move(board):
    """Prompts the human for their move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            r, c = divmod(move, 3)
            if board[r][c] == " ":
                board[r][c] = "X"
                return
            else:
                print("That spot is already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def is_draw(board):
    """Checks if the game is a draw."""
    return all(board[r][c] != " " for r in range(3) for c in range(3))

def main():
    """Main function to run the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X', and the computer is 'O'.")
    print_board(board)
    
    while True:
        # Human turn
        print("Your turn!")
        human_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations, you win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Computer turn
        print("Computer's turn...")
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()