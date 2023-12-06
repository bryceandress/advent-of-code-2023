#with open('example.txt', 'r') as file:
#    content = file.read()

with open('input.txt', 'r') as file:
    content = file.read()
data = ()


times = content.split(':')[1].strip().split()[0:-1]
time = int(''.join(times))
distances = content.split(':')[2].strip().split()
record_dist = int(''.join(distances))

answer = 1
count = 0
for x in range(time):
    distance = x * (time - x)
    if distance > record_dist:
        count += 1
print(count)
