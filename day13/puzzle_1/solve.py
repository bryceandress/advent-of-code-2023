# https://www.youtube.com/watch?v=g3Ms5e7Jdqo never would have gotten this one either
with open('input.txt', 'r') as file:
    grids = file.read().split('\n\n')


def mirror(grid):
    for r in range(1, len(grid)):
        fh = grid[:r][::-1]
        sh = grid[r:]

        fh = fh[:len(sh)]
        sh = sh[:len(fh)]
        if fh == sh:
            return r
    return 0

total = 0

for block in grids:
    grid = block.splitlines()
    row = mirror(grid)
    total += row * 100

    col = mirror(list(zip(*grid)))
    total += col

print(total)
