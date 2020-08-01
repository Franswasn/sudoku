import numpy as np

print("*************************AUTOMATIC SUDOKU SOLVER***************************")


again = 'y'
while again == 'y':
    mat = []
    for i in range(0, 9):
        mat.append([])
    for i in range(0, 9):
        for j in range(0, 9):
            mat[i].append([j])
            mat[i][j] = 0
    for i in range(0, 9):
        for j in range(0, 9):
            while True:
                try:
                    print("Entry in row: ", i + 1, "Entry in column: ", j + 1)
                    mat[i][j] = int(input())
                    if mat[i][j] not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                        raise ValueError
                except ValueError:
                    print("Enter valid number")
                else:
                    break

    print("\n*************************************UNSOLVED SUDOKU***********************")

    print(np.array(mat))
    grid = mat


    # grid = [[0, 4, 0, 0, 1, 0, 9, 0, 8],
    #         [8, 0, 5, 0, 0, 0, 7, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 0],
    #         [0, 2, 0, 0, 0, 5, 0, 0, 4],
    #         [0, 0, 1, 6, 0, 0, 0, 0, 0],
    #         [0, 3, 0, 0, 0, 8, 0, 0, 2],
    #         [0, 0, 0, 0, 0, 0, 0, 6, 0],
    #         [3, 0, 4, 0, 0, 0, 8, 0, 0],
    #         [0, 8, 0, 0, 9, 0, 4, 0, 3]]

    def possible(y, x, n):
        global grid
        for i in range(0, 9):
            if grid[y][i] == n:
                return False
        for i in range(0, 9):
            if grid[i][x] == n:
                return False
        xo = (x // 3) * 3
        yo = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if grid[yo + i][xo + j] == n:
                    return False
        return True


    # print(possible(4,4,5))

    def solve():
        global grid
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1, 10):
                        if possible(y, x, n):
                            grid[y][x] = n
                            solve()
                            grid[y][x] = 0

                    return

        print("\n*************************************SOLVED SUDOKU***********************")
        print(np.array(grid))
    solve()

    again = input("\nTry again:  'y' or 'n'? ")
    if again == 'n':
        exit()




