# get sudokus into a list correctly :)

f = open("problem-096-su-doku/sudoku.txt")
content = f.read()
raw_content = content.split()

grid = []
for line in raw_content:
    grid.append(line)

puzzles = []
for s in range(0,550,11):
    puzzle = []
    for i in range(11):
        if i == 0 or i ==1:
            continue
        pos = s + i
        row = []
        for el in grid[pos]:
            row.append(int(el))
        puzzle.append(row)
    puzzles.append(puzzle)
    

# HELPER functions

def used_in_row(puzzle, row_nr, nr):
    if nr in puzzle[row_nr]:
        return True
    else:
        return False
    


def used_in_col(puzzle, col_nr, nr):
    for i in range(9):
        if puzzle[i][col_nr] == nr:
            return True
    return False

def used_in_box(puzzle, row_nr, col_nr, nr):
    for i in range(3):
        for j in range(3):
            if puzzle[i + row_nr][j+col_nr] == nr:
                return True
    return False


def is_location_safe(puzzle, row_nr, col_nr, nr):
    return (not used_in_row(puzzle, row_nr, nr) and (not used_in_col(puzzle, col_nr, nr) and (not used_in_box(puzzle, row_nr-row_nr%3, col_nr-col_nr%3, nr))))

def find_empty_loc(puzzle, l):
    for row_nr in range(9):
        for col_nr in range(9):
            if puzzle[row_nr][col_nr] == 0:
                l[0] = row_nr
                l[1] = col_nr
                return True
    return False
   
   
   
# main function     
def solve_sudoku(puzzle):
    l = [0,0]
    
    if(not find_empty_loc(puzzle, l)):
        return True
    
    row_nr = l[0]
    col_nr = l[1]
    
    for nr in range(1,10):
        if is_location_safe(puzzle, row_nr, col_nr, nr):
            
            puzzle[row_nr][col_nr] = nr
            
            if solve_sudoku(puzzle):
                return True
            
            puzzle[row_nr][col_nr] = 0
    return False 

answ = 0
for puzzle in puzzles:
    solve_sudoku(puzzle)
    
    n = ''
    for i in range(3):
        n += str(puzzle[0][i])
    answ += int(n)
    
print(answ)
    