#Uses python3

import sys

def explore(v, adj, dp, rec_dp, cycle):
    dp[v] = True
    rec_dp[v] = True
    for ne in adj[v]:
        if ne not in dp:
            dp, cycle = explore(ne, adj, dp, rec_dp, cycle)
            if cycle:
                return dp, 1
        else:
            if rec_dp[ne]:
                return dp, 1
    rec_dp[v] = False
    return dp, 0


def acyclic(adj):
    dp = {}
    cycle = 0
    rec_dp = [False for i in range(len(adj))]
    for node in range(len(adj)):
        dp, cycle = explore(node, adj, dp, rec_dp, cycle)
        if cycle:
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    # print('adj ', adj)
    # adj = [[1, 2, 3], [2, 4], [3, 4], [], []]
    print(acyclic(adj))
