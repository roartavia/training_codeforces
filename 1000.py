# WHERE:  https://codeforces.com/problemset/page/6?order=BY_RATING_ASC
import math

# Theatre Square
# https://codeforces.com/problemset/problem/1/A
# Input
# The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).
# Output
# Write the needed number of flagstones.
listInputs = list(map(int, input().split()))
m, n, a = listInputs[0], listInputs[1], listInputs[2]
print(math.ceil(m/a)*math.ceil(n/a))
# ---------------------------------------------------------------------------------------------------------------------
