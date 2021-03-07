#Uses python3

import sys

def explore(v, adj, dp):
    dp[v] = True
    for V in adj[v]:
        if V not in dp:
            dp = explore(V, adj, dp)
    return dp

def number_of_components(adj):
    count = 0
    #write your code here
    n = len(adj)
    dp = dict()
    for v in range(n):
        if v not in dp:
            count += 1
            dp = explore(v, adj, dp)
    return count



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [4,2,1,2,3,2]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
