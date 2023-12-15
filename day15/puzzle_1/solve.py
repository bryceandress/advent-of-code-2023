#https://www.youtube.com/watch?v=WCVOBKUNc38
with open('input.txt', 'r') as file:
    groups = file.read().strip('\n').split(',')
total = 0
for g in groups:
    inner_total = 0
    for c in g:
        inner_total += ord(c)
        inner_total *= 17
        inner_total %= 256
    total += inner_total
print(total)
