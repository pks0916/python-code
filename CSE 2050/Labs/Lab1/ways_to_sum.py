

def ways_to_sum_memo(n, total, memo=None):
    if memo is None:
        memo = {}

    if total in memo:
        return memo[total]

    if total == 0:
        return 1
    
    

    cnt = 0
    for i in range(1, n + 1):
        if total - i >= 0:
            cnt += ways_to_sum_memo(n, total - i, memo)
    
    memo[total] = cnt
    return cnt

print(ways_to_sum_memo(n=4, total=9)) 



def ways_to_sum_tab(n, total):
    diff_ways_sum = {0:1, 1:1}
    for i in range(2,total+1):
        diff_ways_sum[i] = 0
        for j in range(1, n + 1):
            if i - j >= 0:
                diff_ways_sum[i] += diff_ways_sum[i - j]
    return diff_ways_sum[total]


