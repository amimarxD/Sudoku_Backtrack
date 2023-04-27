import time

grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
	    [4, 0, 7, 0, 0, 0, 2, 0, 8],
	    [0, 0, 5, 2, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 9, 8, 1, 0, 0],
	    [0, 4, 0, 0, 0, 3, 0, 0, 0],
	    [0, 0, 0, 3, 6, 0, 0, 7, 2],
	    [0, 7, 0, 0, 0, 0, 0, 0, 3],
	    [9, 0, 3, 0, 0, 0, 6, 0, 4]]

# grid = [
#         [7,8,0,4,0,0,1,2,0],
#         [6,0,0,0,7,5,0,0,9],
#         [0,0,0,6,0,1,0,7,8],
#         [0,0,7,0,4,0,2,6,0],
#         [0,0,1,0,5,0,9,3,0],
#         [9,0,4,0,6,0,0,0,5],
#         [0,7,0,3,0,0,0,1,2],
#         [1,2,0,0,0,7,4,0,0],
#         [0,4,9,2,0,6,0,0,7]
#     ]
def testAndFind(grid : list, position : tuple, current : int) -> int:
    # Extract the equevalent three by three square (as a list) to the position variable
    pos_x = position[0]//3
    pos_y = position[1]//3
    three_x_three = [grid[i][j] for i in range(pos_x*3,pos_x*3+3) for j in range(pos_y*3,pos_y*3+3)]
    print(three_x_three)

    # Extract the equevalent column (as a list) to the position variable
    column = [grid[i][position[1]] for i in range(9)]

    if current == 0:
        current = 1

    for i in range(current,10):       
        # print(i, " ,", end = "")
        if i not in grid[position[0]]  and  i not in column  and  i not in three_x_three: 
            print()
            return i
    
    print()
    return 0
        


def solve(grid : list) -> list:
    backtracking_list = []
    backtrack = False
    i = 0

    while i < 9:
        j = 0
        # print("i = ", i)
        while j < 9:
            # print("j = ", j)
            if grid[i][j] == 0 or backtrack:
                backtrack = False
                found = testAndFind(grid, (i,j), grid[i][j]+1)
                if found == 0:
                    backtrack = True
                    # print("backtracking list : ", backtracking_list)
                    grid[i][j] = 0
                    i, j = backtracking_list.pop()
                    j -=1
                else:
                    grid[i][j] = found
                    backtracking_list.append((i,j))
                    # print("backtracking list : ", backtracking_list)
                    # print(found, "position : (", i," , ", j, ")")
            # print(grid)
                    
            # print("backtracking list : ", backtracking_list)
            # time.sleep(0.3)
            j += 1
            if j == 9 and found == 0:
                i -= 1

        i += 1
    return grid

solved_grid = solve(grid)

for row in solved_grid:
    print(row)
    
