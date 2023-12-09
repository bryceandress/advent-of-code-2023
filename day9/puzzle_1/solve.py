from itertools import groupby

with open('input.txt', 'r') as file:
    content = file.read().splitlines()


def calc(nums):
    row_answers = []
    l = len(nums)
    itr = 0
    for n in nums:
        try:
            row_answers.append(int(nums[itr+1]) - int(nums[itr]))
            itr += 1
        except IndexError:
            pass
    return row_answers

def check(list):
    return all(i == 0 for i in list)

def solve(big_answers):
    z = 0
    last = 0
    for i in reversed(big_answers):
        z = last + int(i[-1])
        last = z
    return z

real_answer = 0
big_answers = []
for n_row in content:
    nums = n_row.split()
    c = False
    big_answers.append(nums)
    while not c:
        ans = calc(nums)
        c = check(ans)
        big_answers.append(ans)
        nums = ans
print(solve(big_answers))
