'''
Putnam 2007, A3
PROBLEM:
Let k be a positive integer.
Suppose that the integers 1,2,3,...,3k + 1
are written down in random order.
What is the probability that at no time during this process,
the sum of the integers that have been written up to that time
is a positive integer divisible by 3?
'''
import random
from itertools import permutations as perms

MAX_K = 15
TRIALS = 10000

def good(arr):
    curSum = 0
    for x in arr:
        curSum += x
        if curSum%3 == 0:
            return False
    return True

for k in range(1, MAX_K+1):
    print(f"-- k = {k} --")

    ## random
    nums = [i for i in range(1, 3*k+2)] # 1,2,3,...,3k+1
    timesGood = 0
    for t in range(TRIALS):
        random.shuffle(nums)
        if good(nums): timesGood += 1
        #print(nums)
    prop = timesGood / TRIALS
    print(f"random: {timesGood}/{TRIALS} = {100*prop:.3f}%")

    ## testing all permutations
    if k <= 3: #(anything past k=3 will take forever)
        nums = [i for i in range(1, 3*k+2)] # 1,2,3,...,3k+1
        timesGood = 0
        total = 0
        for p in perms(nums):
            if good(p): timesGood += 1
            total += 1
        prop = timesGood / total
        print(f"testing all perms: {timesGood}/{total} = {100*prop:.3f}%")
