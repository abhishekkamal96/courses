#Uses python3

import sys
import queue


def bipartite(adj):
    #write your code here
    visited = {}
    q = queue.Queue(maxsize=len(adj))
    colour = [-1 for i in range(len(adj))]
    for node in range(len(adj)):
        if node not in visited:
            q.put(node)
            colour[node] = True
            while not q.empty():
                u = q.get()
                pcolor = colour[u]
                for v in adj[u]:
                    if u == v:
                        return 0
                    if v not in visited and colour[v] == -1:
                        visited[v] = True
                        colour[v] = not pcolor
                        q.put(v)
                    if pcolor == colour[v]:
                        return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # adj = [[3], [4, 3], [3], [1, 2, 0], [1]]
    # print(adj)
    print(bipartite(adj))
