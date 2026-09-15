"""
Simple Chess Game Application
A basic chess implementation with a command-line interface
"""

class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
    
    def initialize_board(self):
        """Initialize the chess board with starting positions"""
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Black pieces (top)
        board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        board[1] = ['p'] * 8
        
        # White pieces (bottom)
        board[6] = ['P'] * 8
        board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        
        return board
    
    def display(self):
        """Display the current board state"""
        print("\n  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(f"{i} {' '.join([piece if piece else '.' for piece in row])}")
        print()
    
    def is_valid_position(self, row, col):
        """Check if a position is within the board"""
        return 0 <= row < 8 and 0 <= col < 8
    
    def is_white_piece(self, piece):
        """Check if a piece belongs to white"""
        return piece and piece.isupper()
    
    def is_black_piece(self, piece):
        """Check if a piece belongs to black"""
        return piece and piece.islower()
    
    def get_pawn_moves(self, row, col):
        """Get valid moves for a pawn"""
        moves = []
        piece = self.board[row][col]
        
        if self.is_white_piece(piece):  # White pawns move up
            # Forward move
            if self.is_valid_position(row - 1, col) and self.board[row - 1][col] is None:
                moves.append((row - 1, col))
                # Double move from starting position
                if row == 6 and self.board[row - 2][col] is None:
                    moves.append((row - 2, col))
            # Captures
            for dc in [-1, 1]:
                new_col = col + dc
                if self.is_valid_position(row - 1, new_col) and self.is_black_piece(self.board[row - 1][new_col]):
                    moves.append((row - 1, new_col))
        
        else:  # Black pawns move down
            # Forward move
            if self.is_valid_position(row + 1, col) and self.board[row + 1][col] is None:
                moves.append((row + 1, col))
                # Double move from starting position
                if row == 1 and self.board[row + 2][col] is None:
                    moves.append((row + 2, col))
            # Captures
            for dc in [-1, 1]:
                new_col = col + dc
                if self.is_valid_position(row + 1, new_col) and self.is_white_piece(self.board[row + 1][new_col]):
                    moves.append((row + 1, new_col))
        
        return moves
    
    def get_knight_moves(self, row, col):
        """Get valid moves for a knight"""
        moves = []
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        piece = self.board[row][col]
        
        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                target = self.board[new_row][new_col]
                if target is None or (self.is_white_piece(piece) and self.is_black_piece(target)) or \
                   (self.is_black_piece(piece) and self.is_white_piece(target)):
                    moves.append((new_row, new_col))
        
        return moves
    
    def get_rook_moves(self, row, col):
        """Get valid moves for a rook"""
        moves = []
        piece = self.board[row][col]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + dr * i, col + dc * i
                if not self.is_valid_position(new_row, new_col):
                    break
                target = self.board[new_row][new_col]
                if target is None:
                    moves.append((new_row, new_col))
                elif (self.is_white_piece(piece) and self.is_black_piece(target)) or \
                     (self.is_black_piece(piece) and self.is_white_piece(target)):
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        
        return moves
    
    def get_bishop_moves(self, row, col):
        """Get valid moves for a bishop"""
        moves = []
        piece = self.board[row][col]
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + dr * i, col + dc * i
                if not self.is_valid_position(new_row, new_col):
                    break
                target = self.board[new_row][new_col]
                if target is None:
                    moves.append((new_row, new_col))
                elif (self.is_white_piece(piece) and self.is_black_piece(target)) or \
                     (self.is_black_piece(piece) and self.is_white_piece(target)):
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        
        return moves
    
    def get_queen_moves(self, row, col):
        """Get valid moves for a queen (rook + bishop moves)"""
        return self.get_rook_moves(row, col) + self.get_bishop_moves(row, col)
    
    def get_king_moves(self, row, col):
        """Get valid moves for a king"""
        moves = []
        piece = self.board[row][col]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                target = self.board[new_row][new_col]
                if target is None or (self.is_white_piece(piece) and self.is_black_piece(target)) or \
                   (self.is_black_piece(piece) and self.is_white_piece(target)):
                    moves.append((new_row, new_col))
        
        return moves
    
    def get_valid_moves(self, row, col):
        """Get all valid moves for a piece at given position"""
        piece = self.board[row][col]
        if piece is None:
            return []
        
        piece_type = piece.lower()
        
        if piece_type == 'p':
            return self.get_pawn_moves(row, col)
        elif piece_type == 'n':
            return self.get_knight_moves(row, col)
        elif piece_type == 'r':
            return self.get_rook_moves(row, col)
        elif piece_type == 'b':
            return self.get_bishop_moves(row, col)
        elif piece_type == 'q':
            return self.get_queen_moves(row, col)
        elif piece_type == 'k':
            return self.get_king_moves(row, col)
        
        return []
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        """Move a piece from one position to another"""
        if not self.is_valid_position(from_row, from_col) or not self.is_valid_position(to_row, to_col):
            return False
        
        piece = self.board[from_row][from_col]
        if piece is None:
            return False
        
        valid_moves = self.get_valid_moves(from_row, from_col)
        if (to_row, to_col) not in valid_moves:
            return False
        
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        
        # Update king positions
        if piece.lower() == 'k':
            if piece.isupper():
                self.white_king_pos = (to_row, to_col)
            else:
                self.black_king_pos = (to_row, to_col)
        
        return True


class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = 'white'
        self.move_history = []
    
    def switch_player(self):
        """Switch between white and black players"""
        self.current_player = 'black' if self.current_player == 'white' else 'white'
    
    def play(self):
        """Main game loop"""
        print("Welcome to Simple Chess!")
        print("Commands:")
        print("  move <from_row> <from_col> <to_row> <to_col> - Move a piece")
        print("  show - Display the board")
        print("  quit - Exit the game")
        print()
        
        while True:
            self.board.display()
            print(f"Current player: {self.current_player}")
            
            command = input("Enter command: ").strip().lower()
            
            if command == 'quit':
                print("Thanks for playing!")
                break
            
            elif command == 'show':
                continue
            
            elif command.startswith('move'):
                parts = command.split()
                if len(parts) != 5:
                    print("Invalid format. Use: move <from_row> <from_col> <to_row> <to_col>")
                    continue
                
                try:
                    from_row, from_col, to_row, to_col = map(int, parts[1:])
                    
                    piece = self.board.board[from_row][from_col]
                    if piece is None:
                        print("No piece at that position!")
                        continue
                    
                    is_white = self.board.is_white_piece(piece)
                    if (self.current_player == 'white' and not is_white) or \
                       (self.current_player == 'black' and is_white):
                        print(f"That's a {self.current_player.split()[0]} piece, not yours!")
                        continue
                    
                    if self.board.move_piece(from_row, from_col, to_row, to_col):
                        self.move_history.append((from_row, from_col, to_row, to_col))
                        self.switch_player()
                        print("Move successful!")
                    else:
                        print("Invalid move!")
                
                except (ValueError, IndexError):
                    print("Invalid input. Please enter numbers between 0-7.")
            
            else:
                print("Unknown command. Type 'help' for available commands.")


if __name__ == "__main__":
    game = ChessGame()
    game.play()
