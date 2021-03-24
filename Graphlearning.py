from collections import defaultdict as gdict


class Graph:

    def __init__(self):

        self.graph = gdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


def dfs_recursive(graph, v, path=[]):
    path += [v]
    for neighbor in graph[v]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)
    return path


def dfs_non_recursive(graph, start):
    stack, path = [start], []
    while stack:
        v = stack.pop()
        if v in path:
            continue
        path.append(v)
        for neighbor in graph[v]:
            stack.append(neighbor)
    return path


def main():
    g = Graph()
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 0)
    g.addEdge(2, 4)
    # v = int(input("Nhập số đỉnh của đồ thị: "))
    # for i in range(v):
    #     e = int(input('Nhập số cạnh của đỉnh %d: ' % i))
    #     for j in range(e):
    #         n = int(input("Ta có cạnh từ đỉnh %d đến đỉnh " % i))
    #         g.addEdge(i, n)
    # print(g.graph)
    x = int(input("Nhập đỉnh cần duyệt: "))
    print('Kết quả duyệt chiều sâu không dùng đệ quy: ')
    print(dfs_non_recursive(g.graph, x))
    print('\nKết quả duyệt chiều sâu dùng đệ quy: ')
    print(dfs_recursive(g.graph, x))


if __name__ == "__main__":
    main()
