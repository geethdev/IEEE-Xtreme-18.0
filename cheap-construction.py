def count_components(S, T):
    n = len(S)
    positions = []
    
    start = 0
    while True:
        start = S.find(T, start)
        if start == -1:
            break
        positions.append(start)
        start += 1

    if not positions:
        return n + 1  
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    for pos in positions:
        for i in range(pos, pos + len(T) - 1):
            union(i, i + 1)

    components = set(find(i) for i in range(n))
    return len(components)

def find_minimum_lengths(S):
    N = len(S)
    min_lengths = [float('inf')] * (N + 1)

    for length in range(1, N + 1):  
        seen = set()  
        
        for i in range(N - length + 1):  
            T = S[i:i + length]
            if T in seen:
                continue
            seen.add(T)
            
            components = count_components(S, T)
            if components <= N:
                min_lengths[components] = min(min_lengths[components], length)


    result = [length if length != float('inf') else 0 for length in min_lengths[1:]]
    return result


S = input().strip()


result = find_minimum_lengths(S)


print(' '.join(map(str, result)))