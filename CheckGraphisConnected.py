from collections import defaultdict as gdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = gdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def reverseGraph(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def Is_Connected(self):
        visited = [False]*(self.V)
        self.DFSUtil(0, visited)
        if any(i == False for i in visited):
            return False
        g = self.reverseGraph()
        visited = [False]*(self.V)
        g.DFSUtil(0, visited)
        if any(i == False for i in visited):
            return False
        return True

    def connected_components(self):
        from collections import deque
        seen = set()
        for root in range(len(self.graph)):
            if root not in seen:
                seen.add(root)
                component = []
                queue = deque([root])

                while queue:
                    node = queue.popleft()
                    component.append(node)
                    for neighbor in self.graph[node]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)
                yield component


if __name__ == "__main__":
    """Sample 1"""
    g_default = Graph(5)
    g_default.addEdge(0, 1)
    g_default.addEdge(1, 2)
    g_default.addEdge(2, 3)
    g_default.addEdge(3, 0)
    g_default.addEdge(2, 4)
    """Sample 2"""
    g_default1 = Graph(7)
    g_default1.addEdge(0, 1)
    g_default1.addEdge(1, 2)
    g_default1.addEdge(2, 3)
    g_default1.addEdge(3, 0)
    g_default1.addEdge(1, 4)
    g_default1.addEdge(5, 6)
    v = int(input("Nhập số đỉnh của đồ thị(Nhập 0 hoặc 1 để dùng đồ thị mặc định): "))
    if v == 0:
        g = g_default
    elif v == 1:
        g = g_default1
    else:
        g = Graph(v)
        for i in range(v):
            e = int(input('Nhập số cạnh của đỉnh %d: ' % i))
            for j in range(e):
                n = int(input("Ta có cạnh từ đỉnh %d đến đỉnh " % i))
                g.addEdge(i, n)
    print(g.graph)
    if g.Is_Connected():
        print("Đồ thị đã nhập có liên thông!")
    else:
        print("Đồ thị đã nhập Không liên thông!\nCác thành phần liên thông: ")
        for elem in g.connected_components():
            print(elem)
