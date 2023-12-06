import re

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

def part1(infile):
    with open("input.txt") as f:
        engine = f.read().split()
        adj = searchAdjacents(engine)
        return sum([ n for n,p in adj])

print(part1("input.txt"))

