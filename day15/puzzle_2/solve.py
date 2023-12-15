#https://www.youtube.com/watch?v=WCVOBKUNc38
with open('input.txt', 'r') as file:
    groups = file.read().strip('\n').split(',')

def hash(s):
    inner_total = 0
    for c in s:
        inner_total += ord(c)
        inner_total *= 17
        inner_total %= 256
    return inner_total


boxes = [[] for _ in range(256)]
focal_lengths = {}

for instructions in groups:
    if "-" in instructions:
        label = instructions[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = instructions.split("=")
        length = int(length)

        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)

        focal_lengths[label] = length

total = 0

for box_number, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += box_number * lens_slot * focal_lengths[label]

print(total)
