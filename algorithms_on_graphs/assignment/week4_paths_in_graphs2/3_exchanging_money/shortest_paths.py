#Uses python3

import sys
import queue


# ref - https://github.com/parthnatekar/Algorithms-on-Graphs/blob/master/week4_paths2/3_shortest_paths/shortest_paths.py

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    inf = 10**19
    distance[s] = 0
    reachable[s] = 1
    q = queue.Queue()
    for count in range(len(adj)):
        for u in range(len(adj)):
            for vind in range(len(adj[u])):
                v = adj[u][vind]
                if distance[u] != inf and distance[v] > distance[u] + cost[u][vind]:
                    distance[v] = distance[u] + cost[u][vind]
                    reachable[v] = 1
                    if count == len(adj) - 1:
                        q.put(v)

    visited = [0 for i in range(len(adj))]

    # return reachable, shortest, distance


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    s = data[0]
    s -= 1
    # print('adj ', adj)
    # print('cost', cost)
    # print('n', n, 's ', s)
    # n = 5
    # adj = [[1, 2], [2], [4], [2], [3], [0]]
    # cost = [[10, 100], [5], [7], [-18], [10], [-1]]
    # s = 3
    # adj = [[1], [2], [0], [0], []]
    # cost = [[1], [2], [-5], [2], []]

    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

