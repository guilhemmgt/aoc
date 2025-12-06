def is_paper_roll(grid, x, y):
    """
    Returns `True` is these coordinates are valid and designate a paper roll; `False` otherwise
    """
    grid_size = len(grid)
    if x < 0 or y < 0 or x >= grid_size or y >= grid_size:
        return False
    return grid[x][y]


def nb_of_adjacent_paper_rolls(grid, x, y):
    """
    Returns the nb of paper rolls adjacent to a coordinates in all 8 directions
    """
    adjacents_paper_rolls = 0
    for dX in [-1, 0, 1]:
        for dY in [-1, 0, 1]:
            if dX == 0 and dY == 0:
                continue
            adjacents_paper_rolls += is_paper_roll(grid, x + dX, y + dY)
    return adjacents_paper_rolls


def is_accessible(grid, x, y):
    """
    Returns `True` if the coordinate is accessible i.e. have less than 4 adjacent paper rolls; `False` otherwise
    """
    return nb_of_adjacent_paper_rolls(grid, x, y) < 4


def main():
    with open('input') as f:
        input = [line.strip() for line in f]

    grid_size = len(input)
    grid = [
        [input[y][x] == '@' for x in range(0, grid_size)] for y in range(0, grid_size)]

    sum = 0
    for x in range(0, grid_size):
        for y in range(0, grid_size):
            if not is_paper_roll(grid, x, y):
                continue
            sum += is_accessible(grid, x, y)

    print(sum)


if __name__ == '__main__':
    main()
