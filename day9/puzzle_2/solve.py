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
    first = None
    isFirst = True
    for i in reversed(big_answers):
        if isFirst:
            z = int(i[0])
            isFirst  = False
        else:
            z = int(i[0]) - first
        first = z
    return z

real_answer = 0
for n_row in content:
    big_answers = []
    nums = n_row.split()
    c = False
    big_answers.append(nums)
    while not c:
        ans = calc(nums)
        c = check(ans)
        if not c:
            big_answers.append(ans)
        nums = ans
    real_answer += solve(big_answers)
print(real_answer)
