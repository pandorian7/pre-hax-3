n = int(input())
ws = list(map(int, input().split()))

import math

def min_weighings(num_balls, weights):
    # Get the number of distinct weights
    distinct_weights = set(weights)
    k = len(distinct_weights)  # Number of distinct weights

    # Calculate the minimum number of weighings required
    if k == 0:
        return 0  # No weights available
    min_weighs = math.ceil(num_balls * math.log(k, 3))

    return min_weighs

print(min_weighings(n, ws)-1)