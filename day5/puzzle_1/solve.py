with open('input.txt', 'r') as file:
    content = file.read()

#seeds = content..split()split(': ')[1]
seeds = content.split('\n')[0].split(': ')[1].split()

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

def search_in_map(map_data, key, find_me):
    for entry in map_data[key]:
        if int(find_me) in range(int(entry[1]), (int(entry[1]) + int(entry[2]))):
            find_me = int(entry[0]) + (int(find_me) - int(entry[1]))
            return find_me
    return find_me

find_me = None
destinations = []
for seed in seeds:
    find_me = seed
    for _map in map_data.keys():
        find_me = search_in_map(map_data, _map, find_me)
        #print(find_me)
    destinations.append(find_me)

print(sorted(destinations)[0])
# printing the first element
#print("Smallest element is:", destinations[0])
