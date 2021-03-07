#Uses python3

import sys

def dfs(adj, used, order, x, dp):
    #write your code here
    dp[x] = True
    for node in adj[x]:
        if node not in dp:
            used, order, dp = dfs(adj, used, order, node, dp)

    if not used[x]:
        used[x] = 1
        order.append(x)

    return used, order, dp



def toposort(adj):
    used = [0] * len(adj)
    order = []
    dp = {}
    #write your code here
    for x in range(len(adj)):
        used, order, dp = dfs(adj, used, order, x, dp)

    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    # print("adj ", adj)
    # adj = [[1], [], [0], [0]] # working
    # adj = [[], [], [0], []] #
    # adj = [[], [0], [1, 0], [2, 0], [1, 2]] # working
    order = toposort(adj)
    for x in reversed(order):
        print(x + 1, end=' ')

