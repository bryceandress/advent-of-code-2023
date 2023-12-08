import re
import math
from typing import List, Dict


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

pos = []
for node in nodes:
    if node[-1] == "A":
        pos.append(node)

def path(start: str, directions: str, nodes: Dict) -> int:
    pos = start

    steps = 0
    while pos[-1] != "Z":
        direction = directions[steps % n]
        if direction == "L":
            pos = nodes[pos][0]
        else:
            pos = nodes[pos][1]
        steps += 1
    return steps


path_len = [path(p, directions, nodes) for p in pos]
print(path_len)
#for p in path_len:
#    assert c % n == 0
lcm = math.lcm(*path_len)
print(lcm)


