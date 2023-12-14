#https://www.youtube.com/watch?v=WCVOBKUNc38
with open('input.txt', 'r') as file:
    grid = file.read().splitlines()

grid = list(map("".join, zip(*grid)))

grid = ["#".join(["".join(sorted(list(x), reverse=True)) for x in row.split("#")]) for row in grid]
grid = list(map("".join, zip(*grid)))

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))
