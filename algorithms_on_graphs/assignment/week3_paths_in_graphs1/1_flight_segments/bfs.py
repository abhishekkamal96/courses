#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    output = -1
    q = queue.Queue(maxsize=len(adj))
    q.put(s)
    visited = {}
    dist = [0 for i in range(len(adj))]
    visited[s] = True
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if v not in visited:
                visited[v] = True
                q.put(v)
                dist[v] = dist[u] + 1
            if v == t:
                return dist[u] + 1
    return output

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    # adj = [[1, 3, 2], [0, 2], [1, 0], [0]]
    # s = 1
    # t = 3
    # print("adj ", adj, "s", s, 't', t)
    print(distance(adj, s, t))
