def solve_n_queens(n):
    def is_safe(row, col, queens):
        """
        Check if placing a queen at (row, col) is safe:
        - No queens in the same column.
        - No queens on the same diagonal.
        """
        for r, c in queens:
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def place_queen(row, queens, solutions):
        """
        Place queens recursively:
        - If all queens are placed, add the solution.
        - Iterate through columns to find safe positions for the current row.
        """
        if row == n:
            solutions.append(queens[:])  # Store a valid arrangement
            return
        for col in range(n):
            if is_safe(row, col, queens):
                queens.append((row, col))  # Place queen
                place_queen(row + 1, queens, solutions)  # Recur to place next queen
                queens.pop()  # Backtrack: remove the last placed queen

    solutions = []

    # Place the first queen at (0, 0)
    first_queen_position = (0, 0)
    queens = [first_queen_position]
    place_queen(1, queens, solutions)  # Start placing from the next row

    return solutions

def print_solutions(solutions):
    """
    Print each solution as a board:
    - Use 'Q' for queens and '.' for empty spaces.
    """
    for solution in solutions:
        board = [["." for _ in range(n)] for _ in range(n)]  # Create an empty board
        for row, col in solution:
            board[row][col] = "Q"  # Mark queen's position
        for row in board:
            print(" ".join(row))  # Print the board
        print()  # Separate different solutions

if __name__ == "__main__":
    n = int(input("Enter the size of the N-Queens puzzle (n): "))  # Input size
    solutions = solve_n_queens(n)  # Solve the puzzle
    print_solutions(solutions)  # Print the solutions
