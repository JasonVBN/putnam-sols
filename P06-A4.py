'''
Putnam 2006, A4
PROBLEM:
Let S={1,2,...,n} for some integer n > 1.
Say a permutation π of S has a local maximum at k ∈ S if
    (i) π(k) > π(k+1) for k = 1;
    (ii) π(k−1) < π(k) and π(k) > π(k+1) for 1 < k < n;
    (iii) π(k−1) < π(k) for k = n.
(For example, if n = 5 and π takes values at 1,2,3,4,5 of 2,1,4,5,3,
    then π has a local maximum of 2 at k = 1,
    and a local maximum of 5 at k = 4.)
What is the average number of local maxima of a permutation of S,
averaging over all permutations of S?
'''

from itertools import permutations as perms

def numMaxes(arr):
    padded = (0,)+arr+(0,)
    ans = 0
    for k in range(1,len(padded)-1):
        if padded[k-1] < padded[k] and padded[k] > padded[k+1]:
            ans+=1
    return ans

for n in range(1,10+1):
    print(f"-- n = {n} --")
    sumMaxes = 0
    total = 0
    for p in perms(range(1,n+1)):
        sumMaxes += numMaxes(p)
        total += 1
    avg = sumMaxes/total
    print(f"{sumMaxes}/{total} = {avg}")


'''
RESULTS:

-- n = 1 --
1/1 = 1.0
-- n = 2 --
2/2 = 1.0
-- n = 3 --
8/6 = 1.3333333333333333
-- n = 4 --
40/24 = 1.6666666666666667
-- n = 5 --
240/120 = 2.0
-- n = 6 --
1680/720 = 2.3333333333333335
-- n = 7 --
13440/5040 = 2.6666666666666665
-- n = 8 --
120960/40320 = 3.0
-- n = 9 --
1209600/362880 = 3.3333333333333335
-- n = 10 --
13305600/3628800 = 3.6666666666666665

Process finished with exit code 0

'''