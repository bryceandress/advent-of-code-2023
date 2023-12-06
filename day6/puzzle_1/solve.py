#with open('example.txt', 'r') as file:
#    content = file.read()

with open('input.txt', 'r') as file:
    content = file.read()
data = ()

times = content.split(':')[1].strip().split()[0:-1]
distances = content.split(':')[2].strip().split()

data = [(int(times[i]), int(distances[i])) for i in range(0, len(times))]

answer = 1
for time, record_dist in data:
    count = 0
    for x in range(time):
        distance = x * (time - x)
        if distance > record_dist:
            count += 1
    answer *= count
print(answer)
