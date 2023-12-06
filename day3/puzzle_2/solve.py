import re
from collections import defaultdict

def searchAdjacents(engine):
    parts = []
    for j in range(len(engine)):
        for p in re.finditer(r'\d+',engine[j]):
            partnumber = p.group(0) # matched integer
            partstart = p.start() # start position in string
            partend = p.end() # end position in string
            # search for simbol around part number
            s = []
            for y in range( max(j-1,0) , min(j+2,len(engine)) ):
                for x in range( max(partstart-1,0), min(partend+1,len(engine[j])) ):
                    if not engine[y][x].isdigit() and engine[y][x]!=".":
                        s.append( (engine[y][x],(x,y)) )
            if len(s):
                parts.append((int(partnumber),s[0]))
    return parts


def part2(infile):
    with open(infile) as f:
        engine = f.read().split()
        adj = searchAdjacents(engine)
        gears = defaultdict(list)
        for n,(g,X) in adj:
            if g=="*":
                gears[X].append(n)
        return sum([ v[0]*v[1] for X,v in gears.items() if len(v)==2 ])

print(part2("input.txt"))

