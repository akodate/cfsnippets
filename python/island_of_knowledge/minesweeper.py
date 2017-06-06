def minesweeper(matrix):
    coord_range = (-1, 0, 1)
    x_range, y_range = range(len(matrix[0])), range(len(matrix))
    return [[sum(
                [sum([matrix[y+j][x+i] for i in coord_range 
                    if x+i in x_range 
                    and y+j in y_range 
                    and (i != 0 or j != 0)])
                for j in coord_range])
            for x in x_range]
            for y in y_range]