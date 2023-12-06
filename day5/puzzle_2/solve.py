with open('input.txt', 'r') as file:
    content = file.read()
#with open('example.txt', 'r') as file:
#    content = file.read()

inputs = content.split('\n')[0].split(': ')[1].split()

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((int(inputs[i]), int(inputs[i]) + int(inputs[i+1])))

tables = content.split('\n')[2:]
map_data = {}
current_map = None
for line in tables:
    if "map" in line:
        map_data[line.split()[0]] = []
        current_map = line.split()[0]
    else:
        if line != '':
            map_data[current_map].append(tuple(line.split()))

for _map in map_data.keys():
    map_data[_map] = sorted(map_data[_map])

for block in map_data.keys():
    ranges = []
    for line in map_data[block]:
        ranges.append(line)
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            a = int(a)
            b = int(b)
            c = int(c)
            os = max(s,b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s,e))
    seeds = new

print(min(seeds)[0])

#print(sorted(destinations)[0])
# printing the first element
#print("Smallest element is:", destinations[0])
