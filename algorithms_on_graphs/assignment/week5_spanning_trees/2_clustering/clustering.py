#Uses python3
import sys
import math


def get_distance(x1,y1,x2,y2):
    d = (((x2-x1)**2) + ((y2-y1)**2))**.5
    return d


def find(parent, i):
    while i != parent[i]:
        i = parent[i]

    return i


def union(parent, i, j, rank):
    i_id = find(parent, i)
    j_id = find(parent, j)
    if rank[i_id] < rank[j_id]:
        parent[i_id] = j_id
    else:
        parent[j_id] = i_id
        if rank[i_id] == rank[j_id]:
            rank[i_id] += 1

    return parent, rank


def get_edges(x, y):
    n = len(x)
    edges = []
    for i in range(n-1):
        for j in range(i+1, n):
            temp = {}
            temp["n"] = [i,j]
            value = get_distance(x[i], y[i], x[j], y[j])
            temp["v"] = value
            edges.append(temp)

    edges = sorted(edges, key = lambda i: i['v'])
    return edges


def clustering(x, y, k):
    #write your code here
    parent = [i for i in range(0, len(x))]
    rank = [0 for i in range(0, len(x))]
    edges = get_edges(x, y)
    taken = []
    subset_count = len(x)
    if k < len(x):
        for edge_ind in range(len(edges)):
            edge = edges[edge_ind]
            nodes = edge.get("n")
            if find(parent, nodes[0]) != find(parent, nodes[1]):
                taken.append(edge)
                parent, rank = union(parent, nodes[0], nodes[1], rank)
                subset_count -= 1

            if subset_count == k:
                break

        for i in range(edge_ind+1, len(edges)):
            edge = edges[i]
            nodes = edge.get("n")
            if find(parent, nodes[0]) != find(parent, nodes[1]):
                return edge['v']
    else:
        return edges[0].get("v", 0)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    # print('x', x)
    # print('y', y)
    # x = [7, 4, 5, 1, 2, 5, 3, 7, 2, 4, 6, 2]
    # y = [6, 3, 1, 7, 7, 7, 3, 8, 8, 4, 7, 6]
    # k = 3
    # x = [3, 1, 4, 9, 9, 8, 3, 4]
    # y = [1, 2, 6, 8, 9, 9, 11, 12]
    # k = 4
    print("{0:.9f}".format(clustering(x, y, k)))
