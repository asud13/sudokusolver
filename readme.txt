Sudoku Solver with SMT (Z3)

This project provides a Sudoku solver that leverages the power of an SMT (Satisfiability Modulo Theories) solver to generate solutions for Sudoku puzzles.

Instead of solving Sudoku with traditional backtracking or heuristics, this solver encodes the puzzle into logical constraints and uses the Z3 SMT solver (via its online API) to compute valid solutions.

✨ Features

Supports standard 9x9 Sudoku puzzles.

Encodes Sudoku rules and constraints into SMT-LIB format (.smt files).

Uses the Z3 solver to generate solutions automatically.

Allows easy modification of Sudoku puzzles through .smt generator files.

Ensures that all Sudoku rules (row, column, and 3x3 box uniqueness) are respected.

📂 Project Structure
.
├── puzzles/
│   ├── example1.smt   # Example Sudoku puzzle encoding
│   ├── example2.smt   # Another puzzle
│
├── solver.py          # Main script to run solver
├── README.md          # Project documentation


.smt files: Contain Sudoku encodings that describe the puzzle constraints.

solver script: Reads an .smt file, sends it to the Z3 solver, and prints the solved Sudoku grid.

⚙️ How It Works

The Sudoku puzzle is represented in SMT-LIB2 format.

Each cell of the grid is modeled as an integer variable constrained between 1–9.

SMT constraints enforce:

Each row contains numbers 1–9 without repetition.

Each column contains numbers 1–9 without repetition.

Each 3×3 sub-grid contains numbers 1–9 without repetition.

Pre-filled clues remain fixed.

The .smt file is fed to the online Z3 solver, which finds a satisfying assignment (solution).

The result is parsed and displayed as a Sudoku grid.

🚀 Usage

Clone the repository:

git clone https://github.com/asud13/sudokusolver.git
cd sudoku-smt-solver


Run the solver with a given .smt puzzle:

python solver.py puzzles/example1.smt


The solved Sudoku grid will be printed to the console.

📝 Example

Input puzzle (example1.smt):

; Example Sudoku puzzle
(declare-const a1 Int)
(declare-const a2 Int)
; ...
; Puzzle constraints here


Output (solved Sudoku):

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

📖 Requirements

Python 3.x

Internet connection (for online Z3 solver)

requests (if your script uses HTTP calls to the Z3 API)

Install dependencies:

pip install -r requirements.txt

🔮 Future Improvements

Add support for different puzzle sizes (e.g., 4x4, 16x16).

Provide an offline mode using the Z3 Python bindings.

Create a web interface to upload .smt puzzles and visualize solutions.

📜 License

This project is licensed under the MIT License.
