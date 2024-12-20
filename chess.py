import os


board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

pieces = {
    "P": "♙", "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔",
    "p": "♟", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚",
}

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_board():
    """Display the chessboard in the terminal."""
    clear_screen()
    print("   a b c d e f g h")
    print("  +----------------+")
    for i, row in enumerate(board):
        row_display = f"{8 - i} | " + " ".join(pieces.get(cell, cell) for cell in row) + f" | {8 - i}"
        print(row_display)
    print("  +----------------+")
    print("   a b c d e f g h")

def parse_move(move):
    """Convert a move like 'e2 e4' to board indices."""
    try:
        start, end = move.split()
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')
        return (start_row, start_col), (end_row, end_col)
    except ValueError:
        return None

def is_valid_move(start, end, player):
    """Check if a move is valid (simplified version)."""
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]

    
    if (player == "white" and piece.islower()) or (player == "black" and piece.isupper()):
        return False

   
    if 0 <= end_row < 8 and 0 <= end_col < 8:
        return True

    return False

def move_piece(start, end):
    """Move a piece from start to end."""
    start_row, start_col = start
    end_row, end_col = end
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = "."

def main():
    """Main game loop."""
    current_player = "white"
    while True:
        print_board()
        print(f"{current_player.capitalize()}'s turn.")
        move = input("Enter your move (e.g., 'e2 e4'): ").strip()
        if move.lower() in ("quit", "exit"):
            print("Game over!")
            break

        parsed_move = parse_move(move)
        if not parsed_move:
            print("Invalid move format. Use 'e2 e4'.")
            continue

        start, end = parsed_move
        if not is_valid_move(start, end, current_player):
            print("Invalid move. Try again.")
            continue

        move_piece(start, end)

        
        current_player = "black" if current_player == "white" else "white"

if __name__ == "__main__":
    main()
