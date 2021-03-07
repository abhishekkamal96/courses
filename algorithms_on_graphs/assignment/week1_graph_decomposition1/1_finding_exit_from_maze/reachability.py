#Uses python3

import sys

def explore(v, adj, dp, found, y):
    dp[v] = True
    if v == y:
        found = 1
    for V in adj[v]:
        if V not in dp:
            found = explore(V, adj, dp, found, y)
    return found




def reach(adj, x, y):
    #write your code here
    found =  0
    dp = dict()
    found = explore(x, adj, dp, found, y)
    return found

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print('adj ', adj)
    print(reach(adj, x, y))
