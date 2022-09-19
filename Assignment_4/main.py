from Assignment import create_sudoku_csp, print_sudoku_solution, create_map_coloring_csp
from Assignment import *
import Assignment

def main():
    #Create Sudoku
    csp = create_sudoku_csp('hard.txt')
    #Print Sudoku
    print_sudoku_solution(csp.backtracking_search())
    print(f"Number of times BackTrack fails: {csp.count_fail}")
    print(f"Number of times BackTrack is called: {csp.count_backtrack}")    
    
main()