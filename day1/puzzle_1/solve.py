import re

# opening the data file
file = open("input.txt")

# reading the file as a list line by line
content = file.readlines()

# closing the file
file.close()

combine = 0

for line in content:
    match = re.findall(r'\d', line)
    first = str(match[0])
    last = str(match[-1])
    combined = first + last
    combine += int(combined)
print(combine)
