def max_subarray_sum(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for num in arr:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def solve_test_case(n, arr):
    
    pairs = [(arr[i], arr[i+1]) for i in range(0, n, 2)]
    best_sum = float('-inf')

    pairs_to_consider = []
    for i, (x, y) in enumerate(pairs):
        if x < 0 or y < 0:
            pairs_to_consider.append(i)
    
    for mask in range(1 << len(pairs_to_consider)):
        curr_arr = list(arr)
        
        for i in range(len(pairs_to_consider)):
            if mask & (1 << i):
                pair_idx = pairs_to_consider[i]
                curr_arr[pair_idx*2] *= -1
                curr_arr[pair_idx*2 + 1] *= -1
        
        curr_max = max_subarray_sum(curr_arr)
        best_sum = max(best_sum, curr_max)
    
    return best_sum

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve_test_case(n, arr)
    print(result)