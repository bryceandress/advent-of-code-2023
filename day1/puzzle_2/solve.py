import re

# opening the data file
file = open("input.txt")

# reading the file as a list line by line
content = file.readlines()

# closing the file
file.close()

combine = 0

for line in content:
    # replace word with number and leave buffer since oneight needs to become 81 and similar
    line = line.strip()
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")

    # puzzle 1 logic
    match = re.findall(r'\d', line)
    first = str(match[0])
    last = str(match[-1])
    combined = first + last
    combine += int(combined)

print(combine)
