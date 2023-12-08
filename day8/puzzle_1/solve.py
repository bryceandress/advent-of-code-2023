import re

START = "AAA"
END = "ZZZ"
L = "L"
R = "R"

with open('input.txt', 'r') as file:
    content = file.read().splitlines()

directions = content[0]
n = len(directions)

nodes = {}
for c in content[2:]:
    start, left, right = re.findall("([A-Z]+)", c)
    nodes[start] = (left, right)

loc = START
steps = 0

while loc !=  END:
    direction = directions[steps % n]
    if direction == "L":
        loc = nodes[loc][0]
    else:
        loc = nodes[loc][1]
    steps += 1

print(steps)
