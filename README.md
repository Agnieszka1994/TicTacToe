# Tic Tac Toe
Tic-tac-toe is a game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. \

The credential must be provided following the below pattern: \
```
(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)
```
## Get started!
- Download the repository 
- run the program in the command-line
```
TicTacToe> python main.py
```
**The program executes the below steps:** \

- Prints an empty field at the beginning of the game.
- Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a field with the changes if everything is ok.
- Ends the game when someone wins or there is a draw.

## Sample usage
```
---------
| _ O _ |
| X _ _ |
| _ _ _ |
---------
Enter the coordinates:
2 3
This cell is occupied! Choose another one!
Enter the coordinates:
2 1
---------
| _ O _ |
| X _ _ |
| _ X _ |
---------
```
```
---------
| _ _ _ |
| _ _ _ |
| _ _ _ |
---------
Enter the coordinates:
one two
You should enter numbers!
Enter the coordinates:
7 8
Coordinates should be from 1 to 3!
Enter the coordinates:
2 2
---------
| _ _ _ |
| _ X _ |
| _ _ _ |
---------
Enter the coordinates:
```
```
---------
| O O X |
| X X _ |
| _ O _ |
---------
Enter the coordinates:
1 1
---------
| O O X |
| X X _ |
| X O _ |
---------
X wins
```
