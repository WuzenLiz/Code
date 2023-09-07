from collections import defaultdict, deque

def bfs(network, start, exit_gateways):
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in network[current_node]:
            if neighbor not in visited:
                if neighbor in exit_gateways:
                    return current_node, neighbor
                queue.append(neighbor)
                visited.add(neighbor)
    
    return None, None

def find_link_to_sever(network, exit_gateways):
    for node in network:
        for neighbor in network[node]:
            # Temporarily remove the link
            network[node].remove(neighbor)
            network[neighbor].remove(node)
            
            start, end = bfs(network, node, exit_gateways)
            
            # Restore the link
            network[node].add(neighbor)
            network[neighbor].add(node)
            
            if start is None:
                return node, neighbor
    
    return None, None

def SI_can_go_to_exit_gateways(network, SI, exit_gateways):
    queue = deque([SI])
    visited = set()
    visited.add(SI)
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in network[current_node]:
            if neighbor not in visited:
                if neighbor in exit_gateways:
                    return True
                queue.append(neighbor)
                visited.add(neighbor)
    
    return False

# Read initialization data
N, L, E = map(int, input().split())
network = defaultdict(set)
for _ in range(L):
    N1, N2 = map(int, input().split())
    network[N1].add(N2)
    network[N2].add(N1)
exit_gateways = set(int(input()) for _ in range(E))

# Game loop
while True:
    import sys
    SI = int(input())  # Bobnet agent's position
    print(SI, file=sys.stderr)

    if SI_can_go_to_exit_gateways(network, SI, exit_gateways):
        start, end = bfs(network, SI, exit_gateways)
    else:
        start, end = find_link_to_sever(network, exit_gateways)

    network[start].remove(end)
    network[end].remove(start)

    print(start, end)