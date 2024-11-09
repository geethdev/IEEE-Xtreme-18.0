def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    return graph

def find_path(graph, start, end, visited):
    if start == end:
        return [start]
    visited[start] = True
    for next_node in graph[start]:
        if not visited[next_node]:
            path = find_path(graph, next_node, end, visited)
            if path:
                return [start] + path
    return []

def get_steiner_tree(graph, terminals, weights, n):
    included = [False] * n
    total_weight = 0
    
    for terminal in terminals:
        included[terminal] = True
    
    for i in range(len(terminals)):
        for j in range(i + 1, len(terminals)):
            visited = [False] * n
            path = find_path(graph, terminals[i], terminals[j], visited)
            
            for node in path:
                included[node] = True
    
    for i in range(n):
        if included[i]:
            total_weight = (total_weight + weights[i]) % (10**9 + 99999)
            
    return total_weight

def solve(n, weights, edges):
    MOD = 10**9 + 99999
    graph = build_graph(n, edges)
    result = []
    
    for k in range(1, n + 1):
        total = 0
        
        def generate_combinations(pos, size, current_subset):
            nonlocal total
            if len(current_subset) == size:
                weight = get_steiner_tree(graph, current_subset, weights, n)
                total = (total + weight) % MOD
                return
            
            for i in range(pos, n):
                current_subset.append(i)
                generate_combinations(i + 1, size, current_subset)
                current_subset.pop()
        
        generate_combinations(0, k, [])
        result.append(total)
    
    return result

n = int(input())
weights = list(map(int, input().split()))
edges = []
for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))

result = solve(n, weights, edges)
for r in result:
    print(r)