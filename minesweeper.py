def changer_fun(grid, cols, rows):
    # Calculate adjacent mine where there is no "#", store the number in count
    # and change that position to the value of count in string
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '#':
                count = 0
                for i in range(max(0, row - 1), min(rows, row + 2)):
                    for j in range(max(0, col - 1), min(cols, col + 2)):
                        if grid[i][j] == '#':
                            count += 1
                grid[row][col] = str(count) if count > 0 else '0'

    return grid


# Creating the grid manually
grid = [["-", "-", "#", "#", "-"],
        ["-", "#", "-", "-", "-"],
        ["#", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "#"],
        ["-", "-", "#", "-", "-"]]

cols = 5
rows = 5

# Calling the function(changing the grid)
grid = changer_fun(grid, cols, rows)

# Print the grid
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end=' ')
    print()
