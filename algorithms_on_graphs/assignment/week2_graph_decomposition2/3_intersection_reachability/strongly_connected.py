#Uses python3

#submitted on geeks for geeks
import sys

sys.setrecursionlimit(200000)

def explore(v, adj, dp, clock, post):
    if v not in dp:
        dp[v] = True
        clock = clock + 1
        # dp[v][0] = clock
        for node in adj[v]:
            if node not in dp:
                dp, clock, post = explore(node, adj, dp, clock, post)
        clock = clock + 1
        post[v] = clock
    return dp, clock, post


def get_scc(v, adj, scc_nodes, dp_new):
    scc_nodes.append(v)
    dp_new[v] = True
    for node in adj[v]:
        if node not in dp_new:
            scc_nodes, dp_new = get_scc(node, adj, scc_nodes, dp_new)
    return scc_nodes, dp_new


def get_max(post): # todo: we have to modify here, finding max off array
    flag = False
    max_ = 0
    for i in range(len(post)):
        if post[i] and post[i] >= post[max_]:
            flag = True
            max_ = i
    if not flag:
        return -1
    return max_


def drop_from_post(post, drops):
    for node in drops:
        post[node] = False
    return post


def number_of_strongly_connected_components(adj, reversed_adj):
    result = 0
    #write your code here
    clock = 0
    post = [0 for i in range(len(adj))]
    dp = {}
    for v in range(len(adj)):
        dp, clock, post  = explore(v, reversed_adj, dp, clock, post)

    # print('post ', post)

    dp_new  = {}
    while len(dp_new) < len(adj):
        max_node = get_max(post)
        scc_nodes = []
        scc_nodes, dp_new = get_scc(max_node, adj, scc_nodes, dp_new)
        # print('max_node', max_node, 'scc_nodes', scc_nodes)
        post = drop_from_post(post, scc_nodes)
        # print("dropped post ", post)
        result += 1
    return result


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #
    # reversed_adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     reversed_adj[b - 1].append(a - 1)
    # # print('adj ', adj)
    # # print('reversed ', reversed_adj)
    # adj = [[1], [2], [0], [0]]
    # reversed_adj = [[3, 2], [0], [1], []]
    adj = [[], [0], [1, 0], [2, 0], [1, 2]]
    reversed_adj = [[1, 2, 3], [2, 4], [3, 4], [], []]

    print(number_of_strongly_connected_components(adj, reversed_adj))
