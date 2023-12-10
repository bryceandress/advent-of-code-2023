# S/O because I have 0 graph theory knowledge https://www.youtube.com/watch?v=r3i3XE9H4uw
from collections import deque

with open('input.txt', 'r') as file:
    grid = file.read().splitlines()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

seen = {(sr, sc)}
q = deque([(sr,sc)])

while q:
    r, c = q.popleft()
    ch = grid[r][c]

    # Check for upwards motion
    if r > 0 and ch in "S|JL" and grid[r-1][c] in "|7F" and (r - 1, c) not in seen:
        seen.add((r - 1, c))
        q.append((r - 1, c))

    # Check downward motion
    if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r+1, c) not in seen:
        seen.add((r + 1, c))
        q.append((r + 1, c))

    # Left
    if c > 0 and ch in "S-J7" and grid[r][c-1] in "-LF" and (r,c-1) not in seen:
        seen.add((r, c-1))
        q.append((r, c-1))

    # Right
    if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c+1] in "-J7" and (r, c+1) not in seen:
        seen.add((r, c+1))
        q.append((r, c+1))
print(len(seen) // 2)
