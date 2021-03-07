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


def minimum_distance(x, y):
    result = 0.
    parent = [i for i in range(0,len(x))]
    rank = [0 for i in range(0, len(x))]
    edges = get_edges(x, y)
    taken = []
    for edge in edges:
        nodes = edge.get("n")
        if find(parent, nodes[0]) != find(parent, nodes[1]):
            taken.append(edge)
            parent, rank = union(parent, nodes[0], nodes[1], rank)

    for item in taken:
        result = result + item.get("v",0)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    # print("x", x)
    # print('y', y)
    # x = [0, 0, 1, 1]
    # y = [0, 1, 0, 1]
    # x= [0, 0, 1, 3, 3]
    # y= [0, 2, 1, 0, 2]
    print("{0:.9f}".format(minimum_distance(x, y)))
