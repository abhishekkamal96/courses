#Uses python3

import sys
# import queue


def parent(i):
    return (i-1)//2

def leftchild(i):
    return 2*i + 1


def rightchild(i):
    return 2*i + 2


def shiftdown(H, i, size):
    max_index = i
    left = leftchild(i)
    if left < size and H[left]["w"] < H[max_index]["w"]:
        max_index = left
    right = rightchild(i)
    if right < size and H[right]["w"]< H[max_index]["w"]:
        max_index = right
    if i != max_index:
        # swap.append((i, max_index))
        H[i], H[max_index] = H[max_index], H[i]
        H = shiftdown(H, max_index, size)
    return H


def shiftup(H, i, size):
    while i > 0 and H[parent(i)]['w'] > H[i]["w"] and i<size:
        H[i], H[parent] = H[parent], H[i]
        i = parent(i)
    return H


def extract_min(H, size):
    root = None
    if size>0:
        root = H[0]
        H[0] = H[size-1]
        size = size-1
        H = shiftdown(H,0, size)
    return H, root, size


def change_priority(H, i, p, size):
    old = H[i]
    H[i]["w"] = p
    if p < old["w"]:
        H = shiftup(H, i, size)
    else:
        H = shiftdown(H, i, size)
    return H


def build_heap(data):
    size = len(data)

    for i in range(size // 2, -1, -1):
        data = shiftdown(data, i, size)

    return data
#Above of this just operations of min-heap and is not used in this problem.

def get_min_index(dist, visited, s):
    min_ = float('inf')
    out = None
    for i in range(len(dist)):
        if i not in visited:
            if dist[i] < min_:
                min_ = dist[i]
                out = i
    return out


def distance(adj, cost, s, t):
    # write your code here
    size = len(adj)
    # H = [{"n":i, "w": float('inf')} for i in range(size)]
    # H[s]["w"] = 0
    # H = build_heap(H)
    prev = [None for i in range(len(adj))]
    dist = [float('inf') for i in range(len(adj))]
    dist[s] = 0
    visited = {}

    # while len(visited)<len(adj):
        # H, min_, size = extract_min(H, size)
        # if min_:
        #     u = min_.get("n")
        #     for ind in range(len(adj[u])):
        #         v = adj[u][ind]
        #         if dist[v] > dist[u] + cost[u][ind]:
        #             dist[v] = dist[u] + cost[u][ind]
        #             prev[v] = u
    while len(visited) < len(adj):
        # print('visited ', visited)
        # print('dist ', dist)
        u = get_min_index(dist, visited, s)
        if u is not None:
            visited[u] = True
            for ind in range(len(adj[u])):
                v = adj[u][ind]
                if dist[v] > dist[u] + cost[u][ind]:
                    dist[v] = dist[u] + cost[u][ind]
                    prev[v] = u
        else:
            break
    if dist[t] < float('inf'):
        return dist[t]
    return -1


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
    s, t = data[0] - 1, data[1] - 1
    # print("adj ", adj)
    # print('cost', cost)
    # print('s ', s, 't', t)
    
    # adj = [[1, 2], [2], [], [0]]
    # cost = [[1, 5], [2], [], [2]]
    # s,t = 0,2

    # adj = [[1, 2], [2, 3, 4], [1, 4, 3], [], [3]]
    # cost = [[4, 2], [2, 2, 3], [1, 4, 4], [], [1]]
    # s = 0
    # t = 4
    print(distance(adj, cost, s, t))
