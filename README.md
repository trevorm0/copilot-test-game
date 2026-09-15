# Copilot Test Game - Chess

A simple chess game application built with Python. This implementation provides a basic chess experience with a command-line interface.

## Features

- **Full chess piece movement rules** for all piece types (pawns, knights, bishops, rooks, queens, and kings)
- **Move validation** to ensure only legal moves are made
- **Turn-based gameplay** for two players (White and Black)
- **Move history tracking** to keep track of all moves made during the game
- **Command-line interface** for easy interaction

## Piece Movement Rules

- **Pawns**: Move forward one square (or two on first move), capture diagonally
- **Knights**: Move in an L-shape (2 squares in one direction, 1 in perpendicular)
- **Bishops**: Move diagonally any number of squares
- **Rooks**: Move horizontally or vertically any number of squares
- **Queens**: Combine rook and bishop movements
- **Kings**: Move one square in any direction

## How to Play

1. Run the game:
   ```bash
   python chess.py
   ```

2. The board will be displayed with coordinates (0-7 for both rows and columns)

3. To move a piece, use the command:
   ```
   move <from_row> <from_col> <to_row> <to_col>
   ```
   
   Example: `move 6 0 4 0` (moves a pawn from row 6, column 0 to row 4, column 0)

4. Players alternate turns automatically after each valid move

5. Type `show` to display the board again

6. Type `quit` to exit the game

## Board Layout

- Rows: 0-7 (top to bottom)
- Columns: 0-7 (left to right)
- White pieces: UPPERCASE (K, Q, R, B, N, P)
- Black pieces: lowercase (k, q, r, b, n, p)
- Empty squares: .

## Example Game Session

```
  0 1 2 3 4 5 6 7
0 r n b q k b n r
1 p p p p p p p p
2 . . . . . . . .
3 . . . . . . . .
4 . . . . . . . .
5 . . . . . . . .
6 P P P P P P P P
7 R N B Q K B N R

Current player: white
Enter command: move 6 4 4 4
Move successful!
```

## Requirements

- Python 3.6+

## Future Enhancements

- Checkmate detection
- Stalemate detection
- En passant capture
- Castling
- Pawn promotion
- Check detection and highlighting
- Undo move functionality
- Game save/load
- AI opponent

## License

This is a simple educational project for demonstrating Python game development.
