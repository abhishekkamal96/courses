# python3
import queue

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m
        def bfs():
            visited_nodes = set()
            q = queue.Queue()
            q.put((1, None))
            visited_nodes.add((1, None))
            path = []
            parent_dict = dict()
            while not q.empty():
                current_node = q.get()
                if 1 == current_node[0]:
                    for i in range(0, n):
                        if -1 == matching[i]:
                            visited_nodes.add((2, i))
                            parent_dict[(2, i)] = (1, None)
                            q.put((2, i))
                elif 2 == current_node[0]:
                    i = current_node[1]
                    for j in range(m):
                        if 1 == adj_matrix[i][j] and j != matching[i] and not (3, j) in visited_nodes:
                            visited_nodes.add((3, j))
                            parent_dict[(3, j)] = current_node
                            q.put((3, j))
                elif 3 == current_node[0]:
                    j = current_node[1]
                    if not busy_right[j]:
                        previous_node = current_node
                        current_node = (4, j)
                        while True:
                            path.insert(0, (previous_node, current_node))
                            if 1 == previous_node[0]:
                                break
                            current_node = previous_node
                            previous_node = parent_dict[current_node]
                        for element in path:
                            if 2 == element[0][0]:
                                matching[element[0][1]] = element[1][1]
                            elif 3 == element[0][0] and 4 == element[1][0]:
                                busy_right[element[1][1]] = True
                        return True  # There is a path in this case
                    else:
                        for i in range(0, n):
                            if j == matching[i] and not (2, i) in visited_nodes:
                                visited_nodes.add((2, i))
                                parent_dict[(2, i)] = current_node
                                q.put((2, i))

            return False

        while bfs():
            continue
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
