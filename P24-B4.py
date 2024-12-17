'''
Putnam 2024, B4
PROBLEM:
Let n be a positive integer.
Define a sequence a(k):
    a(0)=1
    For k>=0, choose m randomly from the set {1,2,...,n}
    And a(k+1) =
        a(k)+1 if m > a(k)
        a(k) if m = a(k)
        a(k)-1 if m < a(k)
Let E(n) be the expected value of a(n).
What is the lim of E(n)/n as n -> infinity?
'''

import random

TRIALS = 2000
MAX_N = 80
for N in range(1,MAX_N+1):
    S = list(range(1,N+1))
    expval = 0
    for t in range(TRIALS):
        a = 1
        for k in range(N):
            m = random.choice(S)
            a = (a+1) if m>a else (a-1) if m<a else a
        expval += a
    expval /= TRIALS
    print(f"N={N}: expval={expval:.3f}; E/N={expval/N:.3f}")