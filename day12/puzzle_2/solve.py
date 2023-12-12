# https://www.youtube.com/watch?v=g3Ms5e7Jdqo never would have gotten this one either
with open('input.txt', 'r') as file:
    rows = file.read().splitlines()

cache = {}

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    key = (cfg, nums)

    if key in cache:
        return cache[key]

    result = 0

    if cfg[0] in '.?':
        result += count(cfg[1:], nums)
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])
        cache[key] = result
    return result

total = 0

for line in rows:
    cfg, nums = line.split(' ')
    nums = tuple(map(int, nums.split(",")))

    cfg = "?".join([cfg] * 5)
    nums *= 5

    total += count(cfg, nums)

print(total)
